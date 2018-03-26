from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from accounts.forms import SignUpForm
from accounts.models import StudentProfile


def index(request):
    return render(request , 'accounts/index.html' , context=None)

def event(request):
    return render(request , 'accounts/events.html' , context=None)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:index')
    else:
        form = SignUpForm()
    return render(request, 'LoginPageStudent.html', {'form': form})

from django.views.generic.edit import UpdateView


class StudentProfileUpdate(UpdateView):
    model = StudentProfile
    fields = ['linkedin_url' , 'resume']
    template_name = 'profile_form.html'
