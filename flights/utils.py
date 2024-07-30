# flights/utils.py

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_flight_status_email(user, flight):
    subject = f"Flight Status Update for Flight {flight.flight_number}"
    html_message = render_to_string('flight_status_email.html', {'user': user, 'flight': flight})
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = user.email

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
