from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Appointment


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

def bookings_view(request):
	appointments = Appointment.objects.all()
	return render(request, 'bookings.html', {'appointments': appointments})

@login_required
def account_view(request):
	return render(request, 'account.html', {'user': request.user})

@login_required
def my_bookings_view(request):
	appointments = Appointment.objects.filter(member=request.user)
	return render(request, 'my_bookings.html', {'appointments': appointments})
