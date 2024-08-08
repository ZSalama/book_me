from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "myapp/home.html")

def bootstrap(request):
	return render(request, 'myapp/bootstrap.html')
