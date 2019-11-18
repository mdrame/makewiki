from django.contrib import admin
from django.urls import path
# from . import views
from .views import PostView, DetailView, register

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('register/', register , name="register" ),

]
