from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(
        r"(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/", views.index, name="index"
    ),
    path("events/", views.get_events, name="show-events"),
    path("add_venue/", views.add_venue, name="add-venue"),
    path("gentext/", views.generate_text, name="generate-text-file"),
    path("gencsv/", views.generate_csv, name="generate-csv-file"),
    path("genpdf/", views.generate_pdf, name="generate-pdf-file"),
    path("getsubs/", views.list_subscribers, name="list-subscribers"),
]
