from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

# Create your views here.


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    month_name = calendar.month_name[month]
    today_date = date.today()

    if year < 2000 or year > 2099:
        year = today_date.year

    title = f"MyClub Event Calendar - {today_date.day}/{month_name}/{year}"
    cal = HTMLCalendar().formatmonth(year, month)

    return HttpResponse(f"<h1>{title}</h1><p>{cal}</p>")
