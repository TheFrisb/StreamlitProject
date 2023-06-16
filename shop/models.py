from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model): # this is a model that will be used to store product information
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    use_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - ${self.price}' # this is a string representation of the Product model

    class Meta:
        verbose_name = 'Product' # this is the singular name of the model in the admin dashboard
        verbose_name_plural = 'Products' # this is the plural name of the model in the admin dashboard


class RegistrationLink(models.Model): # this is a model that will be used to generate registration links for users
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # this is the date and time the link was created
    updated_at = models.DateTimeField(auto_now=True) # this is the date and time the link was last updated


class Coupon(models.Model): # coupon class
    name = models.CharField(max_length=50)
    percentage_off = models.IntegerField(default=20)
    is_active = models.BooleanField(default=True, verbose_name='Select if this coupon should be active')

    @property
    def get_discount(self):
        return self.percentage_off / 100  


    def __str__(self):
        return f'{self.name} -{self.percentage_off}%'
    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'


class UserProfile(models.Model): # this is a model that will be used to store user profile information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True) # this is the name of the user
    credits_balance = models.IntegerField(default=0) # this is the amount of credits the user has
    notification = models.TextField(null=True, blank=True)
    active_coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    streamlit_token = models.CharField(max_length=100, null=True, blank=True)
    streamlit_token_created_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.name # this is a string representation of the UserProfile model, it will return his email if he has one, or his username if he doesn't (google,facebook logins)
    

class OrderItem(models.Model): # ordered products tied to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    use_count = models.IntegerField()

    def __str__(self):
        if self.user.email == '':
            return f'{self.user.username} - {self.product.name}'
        else:
            return f'{self.user.email} - {self.product.name}'
    class Meta:
        verbose_name = 'Ordered item'
        verbose_name_plural = 'Ordered items'



    


