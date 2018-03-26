from datetime import date, datetime
from time import timezone

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView
from .forms import CreateEventForm
from accounts.models import Event


class EventCreateView(CreateView):
    model = Event
    template_name = 'event_create.html'
    form_class = CreateEventForm

class TodayEventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    def get_queryset(self):
        print(date.today().__str__().split("-")[1])
        return Event.objects.filter( start_date= datetime(2018 , 3 , 24 , 8 , 30))

class FutureEventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    def get_queryset(self):
        return Event.objects.filter( start_date__gt= datetime(2018 , 3 , 24 , 8 , 30) )

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'