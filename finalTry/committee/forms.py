from django import forms
from django.views.generic import CreateView

from accounts.models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name' , 'start_date' , 'duration_in_hrs' , 'price' , 'prize']