from .models import UserProfile
from django.utils import timezone
from datetime import timedelta


def remove_tokens(): # function that removes tokens older than 6 hours.
    current_time = timezone.now()
    time_threshold = current_time - timedelta(hours=6)
    user_profiles = UserProfile.objects.filter(streamlit_token_created_at__lt=time_threshold)

    for user_profile in user_profiles:
        user_profile.streamlit_token = None
        user_profile.save()