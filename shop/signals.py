from django.core import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, OrderItem
from django.contrib.auth.models import User
from .sending_mails import elasticemail


@receiver(post_save, sender=User) # this is a decorator that receives the post_save signal from the User model
def create_profile(sender, instance, created, **kwargs): # this is a function that creates a UserProfile object when a User object is created
    if created:
        if instance.email == '': # if the user didn't provide an email, then use the username as the name
            UserProfile.objects.create(user=instance, name=instance.username)
        else: # if the user provided an email, then use the email as the name
            UserProfile.objects.create(user=instance, name=instance.email)


@receiver(post_save, sender=OrderItem)
def new_order_item(sender, instance, created, **kwargs):
    if created:
        if instance.user.email != '': # only send mail if the user has an email
            elasticemail.new_orderItem_mail(instance)



