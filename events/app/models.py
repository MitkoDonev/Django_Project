from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField("Zip/Post Code", max_length=12)
    phone = models.CharField("Contact Phone", max_length=20)
    web = models.URLField("Web Address")
    email_address = models.EmailField("Email Address")

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField("User Email")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Events(models.Model):
    name = models.CharField("Event Name", max_length=120)
    event_date = models.DateTimeField("Event Date")
    vanue = models.ForeignKey(Venue, blank=True, null=True, on_delete=CASCADE)
    manager = models.CharField(max_length=60)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
