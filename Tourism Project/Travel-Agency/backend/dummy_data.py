import os
import django
from datetime import datetime, date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from login.models import User, Accommodation, HotelBooking, Bookings, HotelReview, HotelComplaint, Package

def create_sample_data():
    hotel_casa = Accommodation.objects.get(id=1)
    cust1 = User.objects.get(id=5) # sanjaips
    cust2 = User.objects.get(id=6) # diya
    cust3 = User.objects.get(id=14) # afia
    guide = User.objects.get(id=16) # akhila
    
    # 1. Direct Bookings
    HotelBooking.objects.get_or_create(
        user=cust1, hotel=hotel_casa,
        check_in_date="2026-04-10", check_out_date="2026-04-15",
        num_rooms=2, total_amount=15000, status="Booked"
    )
    HotelBooking.objects.get_or_create(
        user=cust2, hotel=hotel_casa,
        check_in_date="2026-05-01", check_out_date="2026-05-03",
        num_rooms=1, total_amount=5000, status="Booked"
    )

    # 2. Package Bookings (picked hill casa)
    pkg1 = Package.objects.get(id=3) # Thailand
    pkg2 = Package.objects.get(id=4) # Bali
    
    Bookings.objects.get_or_create(
        user=cust3, package=pkg1, hotel=hotel_casa, guide=guide,
        vacation_date="2026-06-20", num_persons=2, status="Booked"
    )
    Bookings.objects.get_or_create(
        user=cust1, package=pkg2, hotel=hotel_casa, guide=guide,
        vacation_date="2026-07-15", num_persons=3, status="Booked"
    )

    # 3. Reviews
    HotelReview.objects.get_or_create(
        user=cust2, hotel=hotel_casa,
        rating=5, comment="Wonderful stay! The hill view is breathtaking."
    )
    HotelReview.objects.get_or_create(
        user=cust3, hotel=hotel_casa,
        rating=4, comment="Great food and service. Highly recommend the AC rooms."
    )

    # 4. Complaints
    HotelComplaint.objects.get_or_create(
        user=cust1, hotel=hotel_casa,
        subject="AC Leakage",
        description="Water is leaking from the AC in room 204. Please fix it soon.",
        status="Pending"
    )
    HotelComplaint.objects.get_or_create(
        user=cust2, hotel=hotel_casa,
        subject="WiFi Issue",
        description="Internet signal is very weak in the lobby area.",
        status="Investigating"
    )

    print("Sample data for 'hill casa' populated successfully!")

if __name__ == "__main__":
    create_sample_data()
