from django.contrib import admin
from .models import Order, Customer, Menu

# Register your models here.

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Menu)
