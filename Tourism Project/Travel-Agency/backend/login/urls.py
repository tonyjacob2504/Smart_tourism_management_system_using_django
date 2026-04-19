from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

#################################################    User    ################################################################

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.signout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('coordinator/', views.coordinator, name='coordinator'),
    path('add_coordinator/', views.add_coordinator, name='add_coordinator'),
    path('delete_agency/<int:id>/', views.delete_agency, name='delete_agency'),

    path('guide/', views.guide, name='guide'),
    path('delete_guide/<int:id>/', views.delete_guide, name='delete_guide'),
    path('add_guide/', views.add_guide, name='add_guide'),


    path('view_package/', views.view_package, name='view_package'),

    path('package/', views.package, name='package'),
    path('add_package/', views.add_package, name='add_package'),
    path('package_details/<int:id>/', views.package_details, name='package_details'),

    path('user_package/', views.user_package, name='user_package'),

    path('booking/', views.booking, name='booking'),

    path('payment/<int:id>/', views.payment, name='payment'),

    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('coordinator_chat/<int:id>/', views.coordinator_chat, name='coordinator_chat'),

    path('list_user/', views.list_user, name='list_user'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('user_chat/<int:id>/', views.user_chat, name='user_chat'),

    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('feedback/', views.feedback, name='feedback'),

    path('user_bookings/', views.user_bookings, name='user_bookings'),

    path('accept_coordinator/', views.accept_coordinator, name='accept_coordinator'),

    path('accept/<int:id>/', views.accept, name='accept'),
    path('reject/<int:id>/', views.reject, name='reject'),

    path('search/', views.search_packages, name='search_packages'),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),

    path('ml-test/', views.ml_test, name='ml_test'),

    path('manage_accommodation/', views.manage_accommodation, name='manage_accommodation'),
    path('add_accommodation/', views.add_accommodation, name='add_accommodation'),
    path('delete_accommodation/<int:id>/', views.delete_accommodation, name='delete_accommodation'),
    
    path('pending_accommodations/', views.pending_accommodations, name='pending_accommodations'),
    path('approve_accommodation/<int:id>/', views.approve_accommodation, name='approve_accommodation'),
    path('reject_accommodation/<int:id>/', views.reject_accommodation, name='reject_accommodation'),
    path('user_accommodations/', views.user_accommodations, name='user_accommodations'),
    path('hotel_payment/<int:id>/', views.hotel_payment, name='hotel_payment'),
    path('hotel_booking_success/<int:id>/', views.hotel_booking_success, name='hotel_booking_success'),
    path('hotel/<int:id>/', views.hotel_detail, name='hotel_detail'),
    path('hotel/<int:id>/review/', views.submit_hotel_review, name='submit_hotel_review'),
    path('hotel/<int:id>/complaint/', views.submit_hotel_complaint, name='submit_hotel_complaint'),
    path('hotel_register/', views.hotel_register, name='hotel_register'),

    # Destination URLs
    path('manage_destinations/', views.manage_destinations, name='manage_destinations'),
    path('add_destination/', views.add_destination, name='add_destination'),
    path('delete_destination/<int:id>/', views.delete_destination, name='delete_destination'),
    path('user_destinations/', views.user_destinations, name='user_destinations'),

    path('guide_register/', views.guide_register, name='guide_register'),
    path('accept_guide/<int:id>/', views.accept_guide, name='accept_guide'),
    path('reject_guide/<int:id>/', views.reject_guide, name='reject_guide'),

    path('hotel_login/', views.hotel_login, name='hotel_login'),
    path('hotel_dashboard/', views.hotel_dashboard, name='hotel_dashboard'),
    path('hotel_logout/', views.hotel_logout, name='hotel_logout'),
    path('hotel_resolve_complaint/<int:id>/', views.hotel_resolve_complaint, name='hotel_resolve_complaint'),

    path('manage_hotel_reviews/', views.manage_hotel_reviews, name='manage_hotel_reviews'),
    path('delete_review/<int:id>/', views.delete_review, name='delete_review'),
    path('manage_hotel_complaints/', views.manage_hotel_complaints, name='manage_hotel_complaints'),
    path('update_complaint_status/<int:id>/', views.update_complaint_status, name='update_complaint_status'),
    path('manage_hotel_bookings/', views.manage_hotel_bookings, name='manage_hotel_bookings'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)