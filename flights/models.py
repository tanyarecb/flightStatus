from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class Flight(models.Model):
    time = models.DateTimeField()  # DateTimeField for time of flight
    flight_number = models.CharField(max_length=10, unique=True)  # Ensure flight number is unique
    departures = models.CharField(max_length=100)  # Departure city/area
    departing_to = models.CharField(max_length=100)  # Destination
    aircraft = models.CharField(max_length=50)  # Aircraft type
    terminal = models.CharField(max_length=10)  # Terminal information
    status = models.CharField(max_length=50)  # Flight status

    def __str__(self):
        return f"{self.flight_number} - {self.status}"

class Notification(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='notifications')  # Relationship with Flight model
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)  # Automatically set the time when the notification is created

    def __str__(self):
        return f"Notification for {self.flight.flight_number} at {self.sent_at}"

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)  # First name
    last_name = models.CharField(max_length=50, blank=True)  # Last name
    email = models.EmailField(unique=True)  # Email
    address = models.TextField(blank=True)  # Address
    phone_number = models.CharField(max_length=20, blank=True)  # Phone number
    flights = models.ManyToManyField(Flight, related_name='users', blank=True)  # Many-to-many relationship with Flight model

    # Override default related_name attributes
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)

    def __str__(self):
        return self.username
