from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Database
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 

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
  


#Detail view clase base view 
class DetailView(DetailView):
    model = Database
    template_name = 'detail.html'
    # we dont need context_object because we are rendering a specific id
    


# register function route
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created log in!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})


# decorator making sure user is log in to view profile page
@login_required
def profile(request):
    return render(request, 'profile.html') 