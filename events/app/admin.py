from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite

# Register your models here.
from .models import Venue, MyClubUser, Event
from forms.forms import VenueForm


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
    list_display_links = None
    list_editable = list_display
    ordering = ("name",)
    search_fields = ("name", "address")
    inlines = [
        EventInline,
    ]


@admin.register(Event, site=admin_site)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_date", "venue")
    list_filter = ("event_date", "venue")
    ordering = ("-event_date",)
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
