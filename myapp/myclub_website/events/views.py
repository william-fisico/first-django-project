from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

def all_events(request):
    event_list = Event.objects.all()

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
