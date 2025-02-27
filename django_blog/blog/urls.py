from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.test),
path('', views.login, name='login-page'),
path('signup/', views.signup, name='signup-page'),
path('home/', views.home, name='home-page'),
]