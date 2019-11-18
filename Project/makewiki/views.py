from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Database
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
 

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
    



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})


