from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.urls import reverse_lazy

from .models import Venue, MyClubUser, Event


class CreateViewDemo(CreateView):
    model = Event
    template_name = "event_form.html"
    fields = ["name", "event_date", "description"]
    success_url = reverse_lazy("show-events")


class UpdateViewDemo(UpdateView):
    model = Event
    template_name = "event_update_form.html"
    fields = ["name", "event_date", "description"]
    success_url = reverse_lazy("show-events")


class DeleteViewDemo(DeleteView):
    model = Event
    template_name = "event_confirm_delete.html"
    context_object_name = "event"
    success_url = reverse_lazy("show-events")


class ArchiveIndexViewDemo(ArchiveIndexView):
    model = Event
    template_name = "event_archive.html"
    date_field = "event_date"
    allow_future = True


class MonthArchiveViewDemo(MonthArchiveView):
    queryset = Event.objects.all()
    template_name = "event_archive_month.html"
    date_field = "event_date"
    context_object_name = "event_list"
    allow_future = True
    month_format = "%m"


class ListViewDemo(ListView):
    model = Event
    template_name = "event_list.html"
    context_object_name = "all_events"


class DetailViewDemo(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"


class TemplateViewDemo(TemplateView):
    template_name = "cbv_demo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Testing The TemplateView CBV"

        return context
