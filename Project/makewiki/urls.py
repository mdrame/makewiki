from django.contrib import admin
from django.urls import path
# from . import views
from.views import PostView, DetailView

urlpatterns = [
    path('', PostView.as_view()),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
]
