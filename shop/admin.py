from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin): # this is a class that inherits from the ModelAdmin class, and enables us to customize the admin panel for the Product model
    list_display = ['name', 'use_count', 'price']
    search_fields = ['name', 'price']
    list_filter = ['created_at']
    list_per_page = 10


admin.site.register(Product, ProductAdmin) # this registers the Product model with the ProductAdmin class in the admin dashboard
admin.site.register(UserProfile) # this registers the UserProfile model in the admin dashboard
admin.site.register(Coupon)
admin.site.register(OrderItem)
# # admin.site.register(User, UserAdmin)
