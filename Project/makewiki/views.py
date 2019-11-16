from django.shortcuts import render
from django.http import HttpResponse
from .models import Database
from django.views.generic import ListView, DetailView
 

# Create your views here.



# def homeView(request):

#     context = {
#                 'database': Database.objects.all()
#     }

#     return render(request, 'home.html', context)

# create class base view 
class PostView(ListView):
    model = Database
    template_name = 'home.html'
    context_object_name = 'database'
  


class DetailView(DetailView):
    model = Database
    template_name = 'detail.html'
    # we dont need context_object because we are rendering a specific id
    



