from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm

# from  django.contrib.auth import get_user_model
# User = get_user_model()
from accounts.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1' )
