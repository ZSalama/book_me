from django.db import models

# Create your models here

from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import time
import pytz

class Appointment(models.Model):
	TIME_CHOICES = [
		(time(13, 0), '1:00 PM'),
		(time(14, 0), '2:00 PM'),
		(time(15, 0), '3:00 PM'),
		(time(16, 0), '4:00 PM'),
	]

	appointment_id = models.AutoField(primary_key=True)
	date = models.DateField(default=timezone.now)
	time = models.TimeField(choices=TIME_CHOICES, default=timezone.now)
	court = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
	notes = models.TextField(blank=True, null=True)
	member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return f"Appointment {self.appointment_id} on {self.date} at {self.time} (Court {self.court})"

