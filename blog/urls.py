from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views # add views to this file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('category/<str:string>/', views.blog_category_view, name='blog-category-view'),
    path('search/', views.blog_search_view, name='blog-search-view'),
    path('post/<int:pk>/', views.blog_detail_view, name='blog-detail-view'),
]

