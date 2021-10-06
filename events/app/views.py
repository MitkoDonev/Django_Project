from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.core.paginator import Paginator

from datetime import date
import calendar
from calendar import HTMLCalendar
import csv
import io

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from .models import Event, Venue, MyClubUser
from forms.forms import VenueForm

# Create your views here.


def generate_text(request):
    response = HttpResponse(content_type="text/plain")
    response["Content-Discription"] = 'attachment; filename="generate_text.txt"'

    lines = [
        "I will not expose the ignorance of the faculty.\n",
        "I will not conduct my own fire drills.\n",
        "I will not use illigal medication.\n",
    ]

    response.writelines(lines)
    return response


def generate_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Discription"] = 'attachment; filename="generate_csv.csv"'

    writer = csv.writer(response)
    venues = Venue.venues.all()
    writer.writerow(["Venue Name", "Address", "Phone", "Email"])

    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.phone, venue.email_address])

    return response


def generate_pdf(request):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica-Oblique", 14)

    lines = [
        "I will not expose the ignorance of the faculty.",
        "I will not conduct my own fire drills.",
        "I will not use illigal medication.",
    ]

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename="test_data.pdf")


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


def list_subscribers(request):
    paginator = Paginator(MyClubUser.objects.all(), 3)
    page = request.GET.get("page")
    subscribers = paginator.get_page(page)

    return render(request, "subscribers.html", {"subscribers": subscribers})
