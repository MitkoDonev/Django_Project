from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class EventManager(models.Manager):
    def event_type_count(self, event_type):
        return self.filter(name__icontains=event_type).count()


class VenueManager(models.Manager):
    def get_queryset(self):
        return super(VenueManager, self).get_queryset().filter(zip_code="00000")


class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField("Zip/Post Code", max_length=12)
    phone = models.CharField("Contact Phone", max_length=20, blank=True)
    web = models.URLField("Web Address", blank=True)
    email_address = models.EmailField("Email Address", blank=True)
    venues = models.Manager()
    local_venues = VenueManager()

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField("User Email")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Event(models.Model):
    name = models.CharField("Event Name", max_length=120)
    event_date = models.DateTimeField("Event Date")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    description = models.TextField(blank=True)
    objects = EventManager()

    def save(self, *args, **kwargs):
        self.manager = User.objects.get(username="mdonev")
        super(Event, self).save(*args, **kwargs)

    def event_timing(self, date):
        if self.event_date > date:
            return "Event is after this date!"
        elif self.event_date == date:
            return "Event is on the same date!"
        else:
            return "Event is before this date!"

    @property
    def name_slug(self):
        return self.name.lower().replace(" ", "-")

    def __str__(self):
        return self.name
