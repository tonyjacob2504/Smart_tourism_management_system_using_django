from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.timezone import now

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


# Custom user model
class User(AbstractUser):
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField()
    profile = models.ImageField(upload_to="profile/")
    role = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True) # pending, accepted, rejected
    location = models.CharField(max_length=100, null=True, blank=True)
    languages = models.CharField(max_length=255, null=True, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    username = None

    objects = CustomUserManager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.fullname

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


# class Guide(models.Model):
#     fullname = models.CharField(max_length=100, null=True, blank=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=100, null=True, blank=True)
#     address = models.TextField()
#     profile = models.ImageField(upload_to="profile/")
#     password = models.CharField(max_length=100, null=True, blank=True)


class Package(models.Model):
    image = models.ImageField(upload_to="package_images/", null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    person = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    guide = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guide")
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.place} - {self.days} Days - ₹{self.price}"
    

# class PackageImage(models.Model):
#     package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to="package_images/")

#     def __str__(self):
#         return f"Image for {self.package.place}"


class CreditCardPayment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Initiated', 'Initiated'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=255)
    card_number_last4 = models.CharField(max_length=4) 
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Initiated')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.user.email} - {self.status}"

    

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True, blank=True, default='Pending')
    payment = models.ForeignKey(CreditCardPayment, on_delete=models.CASCADE, null=True, blank=True)
    vacation_date = models.DateField(null=True, blank=True)
    num_persons = models.PositiveIntegerField(default=1)
    guide = models.ForeignKey(User, related_name='assigned_guide_bookings', on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey('Accommodation', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    advance_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.status
    

class ChatMessage(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=now)

    class Meta:
        db_table = 'chat_message'
        ordering = ['timestamp'] 

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} searched for {self.query}"


class ChatbotQA(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="accommodation_images/", null=True, blank=True)
    type = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    total_rooms = models.PositiveIntegerField()
    checkin = models.TimeField()
    checkout = models.TimeField()
    price_per_night = models.PositiveIntegerField(default=1000)
    password = models.CharField(max_length=128, null=True, blank=True)
    ROOM_TYPE_CHOICES = [
        ('AC', 'AC'),
        ('Non-AC', 'Non-AC'),
    ]
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='Non-AC')
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.name

class HotelBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_rooms = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.ForeignKey(CreditCardPayment, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, default='Booked')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.hotel.name}"

class HotelReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='hotel_reviews')
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.email} for {self.hotel.name} - Rating: {self.rating}"

class HotelComplaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Investigating', 'Investigating'),
        ('Resolved', 'Resolved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='complaints')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.user.email} against {self.hotel.name} - {self.status}"

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    best_season = models.CharField(max_length=100)
    entry_fees = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
