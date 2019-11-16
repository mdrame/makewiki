from django.shortcuts import render
from django.http import HttpResponse
from .models import Database

# Create your views here.


def homeView(request):

    context = {
                'database': Database.objects.all()
    }

    return render(request, 'home.html', context)