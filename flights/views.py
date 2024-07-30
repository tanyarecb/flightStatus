from django.shortcuts import render
from django.http import JsonResponse
from .models import Flight
from django.core.paginator import Paginator

def flight_status(request):
    flight_list = Flight.objects.all().order_by('time')  # Order by flight time
    paginator = Paginator(flight_list, 10)  # Show 10 flights per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def api_flight_status(request):
    flights = Flight.objects.all().values()
    return JsonResponse(list(flights), safe=False)
