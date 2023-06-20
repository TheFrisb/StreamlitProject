from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views # add views to this file

'''
    These urls are for the shop app
    Each url has a specific url tag as 1st parameter
    The 2nd parameter is the view function that will be called when the url is visited
    The 3rd parameter is the name of the url (used in templates) as url('shop-home') for example..
'''
urlpatterns = [
    path('', views.home, name='shop-home'), 
    path('lv/', views.home, name='shop-home-latvian'),
    path('register/confirm/<str:registration_link>/', views.confirm_user, name='confirm_user'), 
    path('register/', views.register_user, name='register_user'), # add register_user url
    path('login/', views.login_user, name='login_user'), 
    path('logout/', views.logout_user, name='logout_user'), #
    path('change-password/', views.change_password, name='change_password'),
    path('get-streamlit-access/', views.streamlit_dashboard, name='dashboard'),
    path('checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('send-contact-message/', views.send_contact_message, name='send_contact_message'),
    path('apply-coupon/', views.add_coupon, name='add-coupon'),
    path('reduce-credits/', views.reduce_credits, name='reduce_credits'),

]
