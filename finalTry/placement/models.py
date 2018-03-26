from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django import forms
from finalTry import settings
# Create your models here.
from django.forms import ModelForm

class Applicant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    criteria = models.DecimalField(max_digits=4 , decimal_places=2)
    requirement = models.TextField(max_length=260)
    def __str__(self):
        return self.name

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name' , 'email' , 'criteria' , 'requirement']


class PlacementApplyForm(ModelForm):
    company_name = forms.MultipleChoiceField(choices= Company.objects.name  , widget=forms.CheckboxSelectMultiple )
    class Meta:
        model = Applicant
        fields = ['company_name']