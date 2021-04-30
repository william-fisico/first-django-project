from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    teste = venue.web
    return render(request, 'events/show_venue.html', 
        {'venue':venue, 'teste':teste})



def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', 
        {'venue_list':venue_list})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted':submitted})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events_list.html', 
        {'event_list':event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "William"
    month = month.capitalize()
    # Convert month from name to number
    month_number = int(list(calendar.month_name).index(month))

    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get current year
    now = datetime.now()
    current_year = now.year

    # Get current time
    #time = now.strftime('%I:%M:%S %p') # horas:minutos:segundos 12h
    time = now.strftime('%H:%M') # horas:minutos 24h


    return render(request, 'events/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal' : cal,
        'current_year': current_year,
        'time': time,
        })
