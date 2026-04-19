from django.contrib import admin
from .models import User, Package, Bookings, CreditCardPayment, ChatMessage, Feedback, SearchHistory, ChatbotQA

# Register your models here.
admin.site.register(User)
admin.site.register(Package)
admin.site.register(Bookings)
admin.site.register(CreditCardPayment)
admin.site.register(ChatMessage)
admin.site.register(Feedback)
admin.site.register(SearchHistory)
admin.site.register(ChatbotQA)