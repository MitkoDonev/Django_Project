from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar

from .models import Event
from forms.forms import VenueForm

# Create your views here.


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    month_name = calendar.month_name[month]
    today_date = date.today()

    if year < 1900 or year > 2099:
        year = today_date.year

    title = f"MyClub Event Calendar - {today_date.day}/{month_name}/{year}"
    cal = HTMLCalendar().formatmonth(year, month)

    announcements = [
        {"date": "6-10-2020", "announcement": "Club Registration Open"},
        {"date": "4-21-2020", "announcement": "Smith Elected New Club President"},
    ]

    return render(
        request,
        "calendar_base.html",
        {"title": title, "cal": cal, "announcements": announcements},
    )


def get_events(request):
    event_list = Event.objects.all()

    return render(request, "event_list.html", {"event_list": event_list})


def add_venue(request):
    submitted = False

    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_venue/?submitted=True")
    else:
        form = VenueForm()
        if "submitted" in request.GET:
            submitted = True

    return render(request, "add_venue.html", {"form": form, "submitted": submitted})
