from django.core.management.base import BaseCommand
from flights.models import Flight

class Command(BaseCommand):
    help = 'Populate the Flight model with initial data'

    def handle(self, *args, **kwargs):
        Flight.objects.create(
            time='2024-08-01 15:30:00',
            flight_number='AA123',
            departures='New York City',
            departing_to='Los Angeles',
            aircraft='Boeing 737',
            terminal='A1',
            status='On Time'
        )

        Flight.objects.create(
            time='2024-08-01 16:45:00',
            flight_number='BA456',
            departures='London',
            departing_to='Paris',
            aircraft='Airbus A320',
            terminal='B2',
            status='Delayed'
        )

        Flight.objects.create(
            time='2024-08-01 17:00:00',
            flight_number='DL789',
            departures='Atlanta',
            departing_to='Miami',
            aircraft='Boeing 767',
            terminal='C3',
            status='Cancelled'
        )

        Flight.objects.create(
            time='2024-08-01 18:15:00',
            flight_number='UA101',
            departures='San Francisco',
            departing_to='New York City',
            aircraft='Boeing 787',
            terminal='D4',
            status='On Time'
        )

        Flight.objects.create(
            time='2024-08-01 19:30:00',
            flight_number='AF202',
            departures='Paris',
            departing_to='Rome',
            aircraft='Airbus A350',
            terminal='E5',
            status='Delayed'
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated Flight model with initial data'))