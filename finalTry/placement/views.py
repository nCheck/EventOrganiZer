from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from accounts.models import Event
from placement.models import CompanyForm, Company , PlacementApplyForm

app_name = 'placements'
# def empty_slot():
#     dates = Event.objects.filter('start_date')
#     for a in range(0 , dates.__len__() -1 ):
#         if dates[a].hour == dates[a+1] and dates[a].start_date.hour

def recruitment_form(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('accounts:index')
    else:
        form = CompanyForm()
    return render(request, 'placements/rec_form.html', {'form': form})

def placement_form(request):
    if request.method == "POST":
        form = PlacementApplyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('accounts:index')
    else:
        form = PlacementApplyForm()
    return render(request, 'placements/rec_form.html', {'form': form})

def place_index(request):
    return render(request , 'placements/placement_index.html')