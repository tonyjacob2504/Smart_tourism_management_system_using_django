from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import AccommodationForm, DestinationForm
from django.db import models
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import pandas as pd
import joblib
import os
import requests as http_requests



# Create your views here.

def home(request):
    feedbacks = Feedback.objects.all()
    accommodations = Accommodation.objects.filter(status='Accepted')[:6] 
    destinations = Destination.objects.all().order_by('-created_at')[:3] # Show top 3 destinations
    recommendations = []
    if request.user.is_authenticated and request.user.role == "user":
        recommendations = get_personalized_packages(request.user)
    return render(request, 'index.html', {
        'feedbacks': feedbacks, 
        'recommendations': recommendations, 
        'accommodations': accommodations,
        'destinations': destinations
    })

def get_personalized_packages(user):
    # Get booked IDs as a clear list of integers
    booked_package_ids = list(Bookings.objects.filter(user=user).values_list('package_id', flat=True))
    
    # Get user interests (places and searches)
    booked_places = list(Package.objects.filter(id__in=booked_package_ids).values_list('place', flat=True))
    searched_queries = list(SearchHistory.objects.filter(user=user).values_list('query', flat=True))
    interests = set([i for i in booked_places + searched_queries if i and len(str(i)) > 2])
    
    results = []
    
    # 1. Try to find personalized matches
    if interests:
        query = models.Q()
        for interest in interests:
            query |= models.Q(place__icontains=interest)
        
        # Fetch matching packages and filter/limit in Python to avoid MySQL subquery issues
        matching_qs = Package.objects.filter(query).distinct()
        for pkg in matching_qs:
            if pkg.id not in booked_package_ids:
                results.append(pkg)
                if len(results) >= 6:
                    break
    
    # 2. Fallback to trending spots if we need more (at least 3 total)
    if len(results) < 3:
        trending_spots = ['Thailand', 'Maldives', 'Paris', 'Bali', 'Dubai', 'Switzerland', 'Sydney', 'Tokyo']
        spot_query = models.Q()
        for spot in trending_spots:
            spot_query |= models.Q(place__icontains=spot)
            
        trending_qs = Package.objects.filter(spot_query).order_by('?')
        seen_ids = [r.id for r in results] + booked_package_ids
        for pkg in trending_qs:
            if pkg.id not in seen_ids:
                results.append(pkg)
                if len(results) >= 6:
                    break
            
    # 3. Final fallback: just get latest packages
    if len(results) < 6:
        latest_qs = Package.objects.all().order_by('-id')
        seen_ids = [r.id for r in results] + booked_package_ids
        for pkg in latest_qs:
            if pkg.id not in seen_ids:
                results.append(pkg)
                if len(results) >= 6:
                    break
        
    return results









def register(request):
    if request.method == "POST":
        profile = request.FILES.get('image')
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        role = request.POST.get('role')
        pass1 = request.POST.get('pass')
        # pass2 = request.POST.get('pass2')

        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exits")
            return redirect('register')
        
        # if pass1 != pass2:
        #     messages.error(request, "Passwords do not match.")
        #     return redirect('register')
        
        # role = "user"
        user = User.objects.create(profile=profile, fullname=full_name, email=email, phone=phone,role=role, address=address, password=make_password(pass1), status="pending")
        user.save()
        return redirect('login')

    return render(request, 'register.html')


# login page.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # authenticate handles USERNAME_FIELD = "email" correctly with username keyword
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Check for coordinator pending status before logging in
            if getattr(user, 'role', None) == "coordinator" and getattr(user, 'status', None) == "pending":
                messages.error(request, "Your coordinator account is still pending approval by the admin.")
                return redirect("login")
            
            if getattr(user, 'role', None) == "guide" and getattr(user, 'status', None) == "Pending":
                messages.warning(request, "Your guide registration is still under review by the agency.")
                return redirect("login")
            
            if getattr(user, 'role', None) == "guide" and getattr(user, 'status', None) == "Rejected":
                messages.error(request, "Your guide registration has been rejected.")
                return redirect("login")
            
            auth_login(request, user)
            
            if user.is_superuser:
                messages.success(request, "Logged in as Admin!")
                return redirect("dashboard")
            
            role = getattr(user, 'role', 'user')
            if role == "user":
                messages.success(request, "Logged in successfully!")
                return redirect("home")
            elif role == "coordinator" and getattr(user, 'status', None) == "accepted":
                messages.success(request, "Logged in as Coordinator!")
                return redirect("dashboard")
            else:
                return redirect("home")

        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html')




@login_required
def signout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def dashboard(request):
    result = User.objects.filter(role="user")
    return render(request, 'admin/dashboard.html', {'result': result})


def coordinator(request):
    result = User.objects.filter(role="coordinator")
    return render(request, 'admin/coordinator.html', {'result': result})


def accept_coordinator(request):
    result = User.objects.filter(role="coordinator", status="pending")
    return render(request, 'admin/accept_coordinator.html', {'result': result})

def accept(request, id):
    result = get_object_or_404(User, id=id)
    result.status = "accepted"
    result.save()
    return redirect('accept_coordinator')

def reject(request, id):
    result = get_object_or_404(User, id=id)
    result.delete()
    
    return redirect('accept_coordinator')


def add_coordinator(request):
    if request.method == "POST":
        profile = request.FILES.get('image')
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pass1 = request.POST.get('pass')

        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exits")
            return redirect('add_coordinator')
        
        role = "coordinator"
        user = User.objects.create(profile=profile, fullname=full_name, email=email, phone=phone,role=role, address=address, password=make_password(pass1))
        user.save()
        return redirect('coordinator')
    return render(request, 'admin/add_coordinators.html')


def delete_agency(request, id):
    agency = get_object_or_404(User, id=id)
    agency.delete()
    messages.success(request, "Agency deleted successfully")
    return redirect('coordinator')


def guide(request):
    result = User.objects.filter(role="guide")
    return render(request, 'admin/guide.html', {'result': result})

def delete_guide(request, id):
    guide = get_object_or_404(User, id=id)
    guide.delete()
    messages.success(request, "Guide deleted successfully")
    return redirect('guide')



def add_guide(request):
    if request.method == "POST":
        profile = request.FILES.get('image')
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        languages = request.POST.get('languages')
        exp = request.POST.get('exp', 0)
        pass1 = request.POST.get('pass')

        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exits")
            return redirect('add_guide')
        
        role = "guide"
        user = User.objects.create(
            profile=profile, 
            fullname=full_name, 
            email=email, 
            phone=phone,
            role=role, 
            address=address, 
            location=location,
            languages=languages,
            years_of_experience=exp,
            password=make_password(pass1),
            status='Accepted'
        )
        user.save()
        return redirect('guide')
    return render(request, 'admin/add_guide.html')

def guide_register(request):
    if request.method == "POST":
        profile = request.FILES.get('image')
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        languages = request.POST.get('languages')
        exp = request.POST.get('exp', 0)
        pass1 = request.POST.get('pass')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('guide_register')

        user = User.objects.create(
            profile=profile,
            fullname=full_name,
            email=email,
            phone=phone,
            role="guide",
            address=address,
            location=location,
            languages=languages,
            years_of_experience=exp,
            status="Pending",
            password=make_password(pass1)
        )
        messages.success(request, "Registration successful! Wait for agency approval.")
        return redirect('home')
    return render(request, 'guide_register.html')

def accept_guide(request, id):
    guide = get_object_or_404(User, id=id)
    guide.status = 'Accepted'
    guide.save()
    messages.success(request, f"Guide {guide.fullname} accepted successfully!")
    return redirect('guide')

def reject_guide(request, id):
    guide = get_object_or_404(User, id=id)
    guide.status = 'Rejected'
    guide.save()
    messages.warning(request, f"Guide {guide.fullname} rejected.")
    return redirect('guide')

def view_package(request):
    packages = Package.objects.all()
    return render(request, 'admin/package.html', {'packages': packages})

def package(request):
    packages = Package.objects.filter(coordinator=request.user)
    return render(request, 'admin/package.html', {'packages': packages})


def add_package(request):
    guides = User.objects.filter(role="guide")
    print("fffffffff", guides)
    if request.method == "POST":
        image = request.FILES.get('image')
        place = request.POST.get('place')
        person = request.POST.get('person')
        days = request.POST.get('days')
        price = request.POST.get('price')
        guide_id = request.POST.get('guide')

        try:
            guide = User.objects.get(id=guide_id)  # Fetch the User instance
        except User.DoesNotExist:
            messages.error(request, "Invalid guide selected")
            return redirect('add_package')
        user = request.user
        package = Package.objects.create(image=image, place=place, person=person, days=days, price=price, guide=guide, coordinator=user)
        package.save()
        return redirect('package')
    return render(request, 'admin/add_package.html', {'guides': guides})


def package_details(request, id):
    package = get_object_or_404(Package, id=id)
    return render(request, 'user/package_details.html', {'package': package})


def user_package(request):
    packages = Package.objects.all().order_by('price')
    return render(request, 'admin/package.html', {'packages': packages})


def payment(request, id):
    package = Package.objects.get(id=id)
    if request.method == "POST":
        date = request.POST.get('date')
        card_name = request.POST.get('c_name')
        card_number = request.POST.get('c_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        guide_id = request.POST.get('guide')
        hotel_id = request.POST.get('hotel')
        
        # Financial Details
        num_persons = int(request.POST.get('persons', 1))
        # Use values from form or calculate if missing
        total_price = float(request.POST.get('total_price', package.price * num_persons))
        advance_paid = float(request.POST.get('advance_paid', total_price * 0.5))
        balance_amount = float(request.POST.get('balance_amount', total_price - advance_paid))

        if not all([card_name, card_number, expiry_date, cvv]):
            messages.error(request, "All payment fields are required.")
            return redirect('payment', id=id)
        
        payment_obj = CreditCardPayment.objects.create(
            user=request.user,
            card_holder_name=card_name,
            card_number_last4=card_number[-4:],  
            amount_paid=advance_paid, # Paying only advance now
            status='Success'
        )
        
        guide_obj = User.objects.get(id=guide_id) if guide_id else None
        hotel_obj = Accommodation.objects.get(id=hotel_id) if hotel_id else None

        booking_obj = Bookings.objects.create(
            user=request.user, 
            package=package, 
            payment=payment_obj, 
            vacation_date=date, 
            status="Booked",
            num_persons=num_persons,
            total_price=total_price,
            advance_paid=advance_paid,
            balance_amount=balance_amount,
            guide=guide_obj,
            hotel=hotel_obj
        )
        return redirect('home')
    
    guides = User.objects.filter(role="guide")
    hotels = Accommodation.objects.filter(status='Accepted')
    return render(request, 'user/payment.html', {
        'package': package,
        'guides': guides,
        'hotels': hotels
    })


def booking(request):
    result = Bookings.objects.filter(user=request.user).order_by('-created_at')
    hotel_bookings = HotelBooking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user/booking.html', {'result': result, 'hotel_bookings': hotel_bookings})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    current_user = request.user
    
    return render(request, 'user/profile.html', {'profile':current_user})


def edit_profile(request):
    user = request.user  

    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        profile_pic = request.FILES.get('image')  

        
        # Update user details
        user.fullname = full_name
        user.address = address
        user.email = email
        user.phone = phone
        user.save()

        if profile_pic:
            user.profile = profile_pic
            user.save()

        return redirect("profile")  

    return render(request, "user/edit_profile.html", {"user": user})


def coordinator_chat(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    sender = request.user
    package = get_object_or_404(Package, id=id)
    receiver = package.coordinator
    receiver_id = receiver.id
    print(receiver_id)

    # Fetch chat messages between these users
    messages = ChatMessage.objects.filter(
        (models.Q(sender=sender, receiver=receiver_id) |
         models.Q(sender=receiver_id, receiver=sender))
    ).order_by('timestamp')

    if request.method == "POST":
        message_content = request.POST.get("message")

        if message_content:
            # Create and save a new chat message
            ChatMessage.objects.create(
                sender=sender, receiver=receiver, message=message_content
            )
            return redirect('coordinator_chat', id=id)

    return render(request, 'user/chat.html', {"messages": messages, "receiver": receiver})


def list_user(request):
    result = User.objects.filter(role="user")
    return render(request, 'admin/list_user.html', {'result': result})


def manage_users(request):
    result = User.objects.filter(role="user")
    return render(request, 'admin/manage_users.html', {'result': result})


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "User deleted successfully")
    return redirect('manage_users')


def user_chat(request, id):
    sender = request.user
    receiver = get_object_or_404(User, id=id)

    # Fetch chat messages between these users
    messages = ChatMessage.objects.filter(
        (models.Q(sender=sender, receiver=receiver) |
         models.Q(sender=receiver, receiver=sender))
    ).order_by('timestamp')

    if request.method == "POST":
        message_content = request.POST.get("message")

        if message_content:
            ChatMessage.objects.create(sender=sender, receiver=receiver, message=message_content)
            return redirect('user_chat', id=id)

    return render(request, 'user/chat.html', {"messages": messages, "receiver": receiver})


def view_feedback(request):
    result = Feedback.objects.all()
    return render(request, 'admin/view_feedback.html', {'result': result})


def feedback(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        result = Feedback.objects.create(user=request.user, feedback=feedback)
        result.save()
        return redirect('feedback')
    return render(request, 'user/feedback.html')


def user_bookings(request):
    if request.user.is_superuser:
        results = Bookings.objects.all().order_by('-created_at')
    else:
        results = Bookings.objects.filter(package__coordinator=request.user).order_by('-created_at')
    
    return render(request, 'admin/booking.html', {'result': results})

def search_packages(request):
    query = request.GET.get('q', '')
    if query and request.user.is_authenticated:
        SearchHistory.objects.create(user=request.user, query=query)
    
    packages = Package.objects.filter(place__icontains=query) if query else Package.objects.all()
    return render(request, 'admin/package.html', {'packages': packages, 'query': query})

def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower().strip()
        
        qa_pairs = ChatbotQA.objects.all()
        best_match = None
        
        # Keyword extraction
        user_words = set(user_message.split())
        stop_words = {'what', 'is', 'are', 'the', 'in', 'of', 'for', 'to', 'a', 'tell', 'show', 'me', 'about', 'how', 'do', 'i'}
        keywords = [w for w in user_words if w not in stop_words and len(w) > 2]
        
        # 1. Direct match
        for qa in qa_pairs:
            q_lower = qa.question.lower()
            if q_lower in user_message or user_message in q_lower:
                best_match = qa.answer
                break
        
        # 2. Keyword match
        if not best_match and keywords:
            max_matches = 0
            for qa in qa_pairs:
                q_lower = qa.question.lower()
                matches = sum(1 for kw in keywords if kw in q_lower)
                if matches > max_matches:
                    max_matches = matches
                    best_match = qa.answer

        if not best_match:
            best_match = "I'm sorry, I don't have specific information on that. Could you try rephrasing? You can ask about popular spots, booking procedures, or visa requirements!"
            
        return JsonResponse({"response": best_match})
    return JsonResponse({"error": "Invalid request"}, status=400)

def ml_test(request):
    predicted_price = None
    error = None
    weather = None

    # Default form values
    location_input = 'Goa'
    num_days = 4
    num_people = 2
    food_level = 'Premium'
    hotel_rating = 4
    guide_support = 'Yes'
    transport_type = 'Flight'
    season = 'Peak'
    distance_km = 5
    activities_count = 6

    if request.method == "POST":
        location_input = request.POST.get('location', 'Goa')
        try:
            # Extract data from form
            num_days = int(request.POST.get('num_days', 4))
            num_people = int(request.POST.get('num_people', 2))
            food_level = request.POST.get('food_level', 'Premium')
            hotel_rating = int(request.POST.get('hotel_rating', 4))
            guide_support = request.POST.get('guide_support', 'Yes')
            transport_type = request.POST.get('transport_type', 'Flight')
            season = request.POST.get('season', 'Peak')
            distance_km = float(request.POST.get('distance_km', 5))
            activities_count = int(request.POST.get('activities_count', 6))

            # Prepare data for ML prediction
            input_data = pd.DataFrame([{
                "Location": location_input,
                "Num_Days": num_days,
                "Num_People": num_people,
                "Food_Level": food_level,
                "Hotel_Rating": hotel_rating,
                "Guide_Support": guide_support,
                "Transport_Type": transport_type,
                "Season": season,
                "Distance_km": distance_km,
                "Activities_Count": activities_count
            }])

            # Load model and predict price
            model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ml", "tourism_price_model.pkl")
            if os.path.exists(model_path):
                model = joblib.load(model_path)
                prediction = model.predict(input_data)
                predicted_price = f"{prediction[0]:.2f}"
            else:
                error = "Model file not found. Please ensure the model is trained."

            # Fetch weather data from wttr.in (no API key needed)
            try:
                def get_icon(desc):
                    d = desc.lower()
                    if 'sun' in d or 'clear' in d: return '☀️'
                    if 'partly' in d and 'cloud' in d: return '⛅'
                    if 'cloud' in d or 'overcast' in d: return '☁️'
                    if 'rain' in d or 'drizzle' in d: return '🌧️'
                    if 'thunder' in d or 'storm' in d: return '⛈️'
                    if 'snow' in d: return '❄️'
                    if 'fog' in d or 'mist' in d: return '🌫️'
                    if 'wind' in d: return '🌬️'
                    return '🌤️'

                weather_url = f"https://wttr.in/{location_input}?format=j1"
                resp = http_requests.get(weather_url, timeout=5)
                if resp.status_code == 200:
                    w_data = resp.json()
                    current = w_data['current_condition'][0]
                    area = w_data.get('nearest_area', [{}])[0]
                    area_name = area.get('areaName', [{}])[0].get('value', location_input)
                    country = area.get('country', [{}])[0].get('value', '')
                    main_desc = current.get('weatherDesc', [{}])[0].get('value', 'N/A')
                    weather = {
                        'location': f"{area_name}, {country}",
                        'temp_c': current.get('temp_C', 'N/A'),
                        'feels_like': current.get('FeelsLikeC', 'N/A'),
                        'description': main_desc,
                        'icon': get_icon(main_desc),
                        'humidity': current.get('humidity', 'N/A'),
                        'wind_kmph': current.get('windspeedKmph', 'N/A'),
                        'visibility': current.get('visibility', 'N/A'),
                        'uv_index': current.get('uvIndex', 'N/A'),
                        'forecast': [
                            {
                                'date': day.get('date', ''),
                                'max_c': day.get('maxtempC', ''),
                                'min_c': day.get('mintempC', ''),
                                'desc': day['hourly'][4].get('weatherDesc', [{}])[0].get('value', '') if day.get('hourly') else '',
                                'icon': get_icon(day['hourly'][4].get('weatherDesc', [{}])[0].get('value', '') if day.get('hourly') else ''),
                            }
                            for day in w_data.get('weather', [])
                        ]
                    }
            except Exception:
                weather = None  # Weather fetch failed silently

        except Exception as e:
            error = f"Error during prediction: {str(e)}"

    return render(request, 'ml_test.html', {
        'predicted_price': predicted_price,
        'error': error,
        'weather': weather,
        'location_input': location_input,
        'num_days': num_days,
        'num_people': num_people,
        'food_level': food_level,
        'hotel_rating': hotel_rating,
        'guide_support': guide_support,
        'transport_type': transport_type,
        'season': season,
        'distance_km': distance_km,
        'activities_count': activities_count,
    })

def manage_accommodation(request):
    accommodations = Accommodation.objects.filter(status='Accepted')
    return render(request, 'admin/manage_accommodation.html', {'accommodations': accommodations})

def pending_accommodations(request):
    accommodations = Accommodation.objects.filter(status='Pending')
    return render(request, 'admin/pending_accommodations.html', {'accommodations': accommodations})

def approve_accommodation(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    accommodation.status = 'Accepted'
    accommodation.save()
    messages.success(request, f"{accommodation.name} approved successfully!")
    return redirect('pending_accommodations')

def reject_accommodation(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    accommodation.delete() # Or set to 'Rejected'
    messages.success(request, f"{accommodation.name} rejected successfully!")
    return redirect('pending_accommodations')

def hotel_register(request):
    if request.method == 'POST':
        form = AccommodationForm(request.POST, request.FILES)
        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.status = 'Pending'
            accommodation.save()
            messages.success(request, "Registration successful! Waiting for admin approval.")
            return redirect('home')
    else:
        form = AccommodationForm()
    return render(request, 'hotel_register.html', {'form': form})

def user_accommodations(request):
    accommodations = Accommodation.objects.filter(status='Accepted')
    return render(request, 'user/accommodations.html', {'accommodations': accommodations})

def hotel_payment(request, id):
    hotel = get_object_or_404(Accommodation, id=id)
    if request.method == "POST":
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        num_rooms = int(request.POST.get('num_rooms', 1))
        card_name = request.POST.get('c_name', request.user.fullname or "N/A")
        card_number = request.POST.get('c_number', '0000000000000000') or '0000000000000000'
        
        # Simple date calculation for total price (idealized)
        from datetime import datetime
        d1 = datetime.strptime(check_in, "%Y-%m-%d")
        d2 = datetime.strptime(check_out, "%Y-%m-%d")
        nights = (d2 - d1).days
        if nights < 1: nights = 1
        
        total_price = hotel.price_per_night * num_rooms * nights

        payment = CreditCardPayment.objects.create(
            user=request.user,
            card_holder_name=card_name,
            card_number_last4=card_number[-4:],
            amount_paid=total_price,
            status='Success'
        )
        
        booking = HotelBooking.objects.create(
            user=request.user,
            hotel=hotel,
            check_in_date=check_in,
            check_out_date=check_out,
            num_rooms=num_rooms,
            total_amount=total_price,
            payment=payment,
            status='Booked'
        )
        messages.success(request, f"Hotel {hotel.name} booked successfully!")
        return redirect('hotel_booking_success', id=booking.id)

    return render(request, 'user/hotel_payment.html', {'hotel': hotel})

def hotel_booking_success(request, id):
    booking = get_object_or_404(HotelBooking, id=id)
    return render(request, 'user/hotel_booking_success.html', {'booking': booking})

def add_accommodation(request):
    if request.method == 'POST':
        form = AccommodationForm(request.POST, request.FILES)
        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.status = 'Accepted' # Admin/Coordinator adding directly should be accepted
            accommodation.save()
            messages.success(request, "Accommodation added successfully!")
            return redirect('manage_accommodation')
    else:
        form = AccommodationForm()
    return render(request, 'admin/add_accommodation.html', {'form': form})

def delete_accommodation(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    accommodation.delete()
    messages.success(request, "Accommodation deleted successfully!")
    return redirect('manage_accommodation')

def hotel_detail(request, id):
    hotel = get_object_or_404(Accommodation, id=id)
    reviews = hotel.hotel_reviews.all().order_by('-created_at')
    # Use filter to avoid error if multiple bookings exist
    has_stayed = HotelBooking.objects.filter(user=request.user, hotel=hotel).exists()
    return render(request, 'user/hotel_detail.html', {
        'hotel': hotel,
        'reviews': reviews,
        'has_stayed': has_stayed
    })

def submit_hotel_review(request, id):
    if request.method == "POST":
        hotel = get_object_or_404(Accommodation, id=id)
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment', '')
        
        HotelReview.objects.create(
            user=request.user,
            hotel=hotel,
            rating=rating,
            comment=comment
        )
        messages.success(request, "Thank you for your review!")
        return redirect('hotel_detail', id=id)
    return redirect('user_accommodations')

def manage_hotel_reviews(request):
    reviews = HotelReview.objects.select_related('user', 'hotel').all().order_by('-created_at')
    return render(request, 'admin/manage_reviews.html', {'reviews': reviews})

def delete_review(request, id):
    review = get_object_or_404(HotelReview, id=id)
    review.delete()
    messages.success(request, "Review deleted.")
    return redirect('manage_hotel_reviews')

def manage_hotel_complaints(request):
    complaints = HotelComplaint.objects.select_related('user', 'hotel').all().order_by('-created_at')
    return render(request, 'admin/manage_complaints.html', {'complaints': complaints})

def update_complaint_status(request, id):
    complaint = get_object_or_404(HotelComplaint, id=id)
    if request.method == "POST":
        complaint.status = request.POST.get('status')
        complaint.save()
        messages.success(request, "Complaint status updated.")
        return redirect('manage_hotel_complaints')
    return redirect('manage_hotel_complaints')

def manage_hotel_bookings(request):
    bookings = HotelBooking.objects.select_related('user', 'hotel', 'payment').all().order_by('-created_at')
    return render(request, 'admin/manage_hotel_bookings.html', {'bookings': bookings})

def submit_hotel_complaint(request, id):
    if request.method == "POST":
        hotel = get_object_or_404(Accommodation, id=id)
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        
        HotelComplaint.objects.create(
            user=request.user,
            hotel=hotel,
            subject=subject,
            description=description
        )
        messages.warning(request, "Complaint submitted. We'll look into it.")
        return redirect('hotel_detail', id=id)
    return redirect('user_accommodations')

def manage_destinations(request):
    destinations = Destination.objects.all().order_by('-created_at')
    return render(request, 'admin/manage_destinations.html', {'destinations': destinations})

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination added successfully!")
            return redirect('manage_destinations')
    else:
        form = DestinationForm()
    return render(request, 'admin/add_destination.html', {'form': form})

def delete_destination(request, id):
    destination = get_object_or_404(Destination, id=id)
    destination.delete()
    messages.success(request, "Destination deleted successfully!")
    return redirect('manage_destinations')

def user_destinations(request):
    destinations = Destination.objects.all().order_by('-created_at')
    return render(request, 'user/destinations.html', {'destinations': destinations})

def hotel_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        hotel = Accommodation.objects.filter(email=email).first()
        if hotel and hotel.password == password:
            if hotel.status != 'Accepted':
                messages.warning(request, "Your hotel registration is still pending approval.")
                return redirect('hotel_login')
            
            # Use session to track hotel login
            request.session['hotel_id'] = hotel.id
            messages.success(request, f"Welcome back, {hotel.name}!")
            return redirect('hotel_dashboard')
        else:
            messages.error(request, "Invalid hotel credentials. Please check your email and password.")
            return redirect('hotel_login')
    return render(request, 'hotel_login.html')

def hotel_dashboard(request):
    hotel_id = request.session.get('hotel_id')
    if not hotel_id:
        return redirect('hotel_login')
    
    hotel = get_object_or_404(Accommodation, id=hotel_id)
    # Get direct bookings and package bookings
    direct_bookings = HotelBooking.objects.filter(hotel=hotel).order_by('-created_at')
    package_bookings = Bookings.objects.filter(hotel=hotel).order_by('-created_at')
    
    # Get reviews and complaints
    reviews = HotelReview.objects.filter(hotel=hotel).order_by('-created_at')
    complaints = HotelComplaint.objects.filter(hotel=hotel).order_by('-created_at')
    
    # Calculate avg rating
    from django.db.models import Avg
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 5.0
    
    return render(request, 'hotel_dashboard.html', {
        'hotel': hotel, 
        'direct_bookings': direct_bookings,
        'package_bookings': package_bookings,
        'reviews': reviews,
        'complaints': complaints,
        'avg_rating': round(avg_rating, 1)
    })

def hotel_logout(request):
    if 'hotel_id' in request.session:
        del request.session['hotel_id']
    return redirect('home')

def hotel_resolve_complaint(request, id):
    hotel_id = request.session.get('hotel_id')
    if not hotel_id:
        return redirect('hotel_login')
    
    complaint = get_object_or_404(HotelComplaint, id=id, hotel_id=hotel_id)
    complaint.status = 'Resolved'
    complaint.save()
    messages.success(request, "Complaint marked as resolved. Good job!")
    return redirect('hotel_dashboard')

