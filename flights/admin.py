from django.contrib import admin
from .models import Flight, User, Notification

admin.site.register(Flight)
admin.site.register(User)
admin.site.register(Notification)