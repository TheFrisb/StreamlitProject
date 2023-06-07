from django.core import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPost, BlogCategory

