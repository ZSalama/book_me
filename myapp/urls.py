from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path("", views.index, name="index"),
	path('bootstrap/', views.bootstrap, name='bootstrap'),
	path('register/', views.register, name='register'),
	path('bookings/', views.bookings_view, name='bookings'),
	path('account/', views.account_view, name='account'),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('account/my_bookings/', views.my_bookings_view, name='my_bookings'),
]
