from django.core.management.base import BaseCommand
from flights.models import Flight, User

class Command(BaseCommand):
    help = 'Insert sample data into the database'

    def handle(self, *args, **kwargs):
        # Sample flight instances
        flight1 = Flight.objects.get(flight_number='AA123')
        flight2 = Flight.objects.get(flight_number='BA456')
        flight3 = Flight.objects.get(flight_number='DL789')

        # Create sample users
        user1 = User.objects.create_user(
            username='john_doe',
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            address='123 Elm Street, Springfield',
            phone_number='555-1234',
            password='securepassword123'
        )

        user2 = User.objects.create_user(
            username='jane_smith',
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            address='456 Oak Avenue, Springfield',
            phone_number='555-5678',
            password='anothersecurepassword'
        )

        user3 = User.objects.create_user(
            username='bob_johnson',
            first_name='Bob',
            last_name='Johnson',
            email='bob.johnson@example.com',
            address='789 Pine Road, Springfield',
            phone_number='555-8765',
            password='yetanotherpassword'
        )

        # Associate users with flights
        user1.flights.add(flight1, flight2)  # User 1 is associated with Flight AA123 and BA456
        user2.flights.add(flight2, flight3)  # User 2 is associated with Flight BA456 and DL789
        user3.flights.add(flight1)           # User 3 is associated with Flight AA123

        self.stdout.write(self.style.SUCCESS('Sample data inserted successfully'))
