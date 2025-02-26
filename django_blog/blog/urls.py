from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
path('login/', views.login, name='login-page'),
path('signup/', views.signup, name='signup-page'),
]