# Flight Status and Notifications

## Project Description
This project provides real-time flight status updates and notifications to passengers. Built with Django for the backend and HTML, CSS, Bootstrap for the frontend.

## Tech Stack
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: SQL
- **Notifications**: send mail through SMTP

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Additional Tools
- **Celery**: For background tasks.
- **Django Signals**: For triggering notifications on flight status changes.

## Usage
1. Navigate to the home page to view flight status.
2. Notifications will be sent via the configured notification system on status changes.
