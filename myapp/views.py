from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.

def index(request):
	return render(request, "myapp/home.html")

def bootstrap(request):
	return render(request, 'myapp/bootstrap.html')

def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
	else:
		form = CustomUserCreationForm()

	return render(request, 'register.html', {'form': form})
