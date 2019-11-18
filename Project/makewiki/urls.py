from django.contrib import admin
from django.urls import path
# from . import views
from .views import PostView, DetailView, register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('register/', register , name="register" ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html') , name="login" ),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html') , name="logout" ),
    path('profile/', profile , name="profile"),

]
