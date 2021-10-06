from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .admin import admin_site
from . import views
from .demo_views import (
    TemplateViewDemo,
    ListViewDemo,
    DetailViewDemo,
    CreateViewDemo,
    UpdateViewDemo,
    DeleteViewDemo,
    ArchiveIndexViewDemo,
    MonthArchiveViewDemo,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", RedirectView.as_view(url="/", permanent=True)),
    path("cbvdemo/", TemplateViewDemo.as_view()),
    path("eventarchive/", ArchiveIndexViewDemo.as_view(), name="event-index"),
    path(
        "<int:year>/<int:month>/",
        MonthArchiveViewDemo.as_view(),
        name="event-montharchive",
    ),
    re_path(
        r"(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/", views.index, name="index"
    ),
    # path("events/", views.get_events, name="show-events"),
    path("events/", ListViewDemo.as_view(), name="show-events"),
    path("event/<int:pk>/", DetailViewDemo.as_view(), name="event-detail"),
    path("event/add/", CreateViewDemo.as_view(), name="add-event"),
    path("event/update/<int:pk>/", UpdateViewDemo.as_view(), name="update-event"),
    path("event/delete/<int:pk>/", DeleteViewDemo.as_view(), name="delete-event"),
    path("add_venue/", views.add_venue, name="add-venue"),
    path("gentext/", views.generate_text, name="generate-text-file"),
    path("gencsv/", views.generate_csv, name="generate-csv-file"),
    path("genpdf/", views.generate_pdf, name="generate-pdf-file"),
    path("getsubs/", views.list_subscribers, name="list-subscribers"),
    path("eventsadmin/", admin_site.urls),
]
