from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
from django.http import HttpResponse
from django import forms

from ckeditor.widgets import CKEditorWidget

import csv

# Register your models here.
from .models import Venue, MyClubUser, Event
from forms.forms import VenueForm


class EventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Event
        fields = "__all__"


def venue_csv(modeladmin, request, quaryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Discription"] = 'attachment; filename="venue_export.csv'
    writer = csv.writer(response)
    writer.writerow(["name", "event_date", "venue", "description"])

    for record in quaryset:
        record_list = []
        record_list.append(record.name)
        record_list.append(record.event_date.strftime("%m/%d/%Y, %H:%M"))
        record_list.append(record.venue.name)
        record_list.append(record.description)
        writer.writerow(record_list)

    return response


venue_csv.short_description = "Export Selected Venues to CSV"


class EventInline(admin.TabularInline):
    model = Event
    fileds = ("name", "event_date")
    extra = 1


class AttendeeInline(admin.TabularInline):
    model = Event.attendees.through
    verbose_name = "Attendee"
    verbose_name_plural = "Attendees"


class EventsAdmin(AdminSite):

    site_header = "MyClub Events Administration"
    site_title = "MyClub Events Admin"
    index_title = "MyClub Events Admin Home"


admin_site = EventsAdmin(name="eventsadmin")
admin_site.register(User)
admin_site.register(Group)


@admin.register(Venue, site=admin_site)
class VenueAdmin(admin.ModelAdmin):
    form = VenueForm
    list_display = ("name", "address", "phone")
    # list_display_links = None
    # list_editable = list_display
    ordering = ("name",)
    search_fields = ("name", "address")
    inlines = [
        EventInline,
    ]

    def get_list_display(self, request):
        return ("name", "address", "phone", "web")


def set_manager(modeladmin, request, quaryset):
    quaryset.update(manager=request.user)


set_manager.short_description = "Manage selected events"


@admin.register(Event, site=admin_site)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ("name", "event_date", "venue", "manager")
    list_filter = ("event_date", "venue")
    ordering = ("-event_date",)
    actions = [set_manager, venue_csv]
    save_as = True
    fieldsets = (
        (
            "Required Information",
            {
                "description": "These fields are required for each event.",
                "fields": (("name", "venue"), "event_date"),
            },
        ),
        (
            "Optional Information",
            {"classes": ("collapse",), "fields": ("description", "manager")},
        ),
    )
    inlines = [
        AttendeeInline,
    ]


admin.site.register(MyClubUser)
