# flights/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Flight, User
from .utils import send_flight_status_email

@receiver(post_save, sender=Flight)
def flight_status_changed(sender, instance, **kwargs):
    if kwargs.get('created', False):
        return

    # Check if the status has changed to "Cancelled" or "Delayed"
    if instance.status in ['Cancelled', 'Delayed']:
        # Get users associated with this flight
        users = User.objects.filter(flights=instance)

        for user in users:
            send_flight_status_email(user, instance)
