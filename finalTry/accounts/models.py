from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_committee = models.BooleanField('committee status', default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE ,related_name='student_profile')
    linkedin_url = models.URLField(verbose_name="website")
    resume = models.FileField(upload_to="resumes", blank=True)

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('accounts:index')


class Event(models.Model):
    name = models.CharField(max_length=50 , blank=True)
    start_date = models.DateTimeField(default=None , blank=False , unique=True)
    duration_in_hrs = models.SmallIntegerField(default=0 , blank=True)
    price = models.SmallIntegerField(default=0 , blank=True)
    prize = models.SmallIntegerField(default=0 , blank=True)
    is_approved = models.BooleanField(default=False , blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:index')

class CommitteeProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='committee_profile')
    name = models.CharField(max_length=50 , blank=True)
    events = models.ManyToManyField(Event , related_name='events')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student_profile.save()