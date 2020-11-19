from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, request, request, request
from django.contrib.auth.decorators import login_required
from .models import Cevent
from dashboard.models import Cmember, Cteam
from accounts import models
from .forms import CteamForm
# Create your views here.


@login_required(login_url='/accounts/login')
def dashboard(request):
    current_user = request.user
    print(current_user.id)
    return render(request, 'dashboard.html')


def cevent(request):
    current_user = request.user
    if request.method == 'POST':
        cevent = Cevent()
        cevent.user_id = current_user.id
        cevent.event_name = request.POST['event_name']
        cevent.event_date = request.POST['event_date']
        cevent.event_time = request.POST['event_time']
        cevent.event_type = request.POST['event_type']
        cevent.event_category = request.POST['event_category']
        cevent.event_website = request.POST['event_website']
        cevent.event_description = request.POST['event_description']
        cevent.save()
    return render(request, 'cevent.html')


def myevent(request):
    current_user = request.user
    # events = Cevent.objects.all()
    events = Cevent.objects.filter(
        user_id__startswith=current_user.id).values()
    return render(request, 'myevent.html', {'events': events, 'current_user': current_user})


def devent(request):
    current_user = request.user
    events = Cevent.objects.all()
    return render(request, 'devent.html', {'events': events, 'current_user': current_user})


def delete_event(request, pk):
    Cevent.objects.filter(id=pk).delete()
    Cteam.objects.filter(event_id=pk).delete()
    current_user = request.user
    events = Cevent.objects.all()
    return render(request, 'devent.html', {'events': events, 'current_user': current_user})


def cteam(request):
    current_user = request.user
    events = Cevent.objects.all()
    if request.method == 'POST':
        cteam = Cteam()
        cteam.user_id = current_user.id
        cteam.event_id = request.POST['event_id']
        cteam.team_name = request.POST['team_name']
        cteam.team_ptask = request.POST['team_ptask']
        cteam.team_description = request.POST['team_description']
        cteam.save()
    return render(request, 'cteam.html', {'events': events, 'current_user': current_user})


def selectteam(request):
    return render(request, "selectteam.html")


def myteam(request):
    current_user = request.user
    print(current_user.id)
    events = Cevent.objects.all()
    teams = Cteam.objects.all()
    return render(request, 'myteam.html', {'events': events, 'current_user': current_user, 'teams': teams})


def dteam(request):
    current_user = request.user
    print(current_user.id)
    events = Cevent.objects.all()
    teams = Cteam.objects.all()
    return render(request, 'dteam.html', {'events': events, 'current_user': current_user, 'teams': teams})


def delete_team(request, pk):
    Cteam.objects.filter(id=pk).delete()
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.all()
    return render(request, 'dteam.html', {'events': events, 'current_user': current_user, 'teams': teams})


def eteam(request, pk):
    teamse = get_object_or_404(Cteam, pk=pk)
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.all()
    if request.method == "POST":
        form = CteamForm(request.POST, instance=teamse)
        if form.is_valid():
            form.save()
            return redirect('myteam')
    else:
        form = CteamForm(instance=teamse)
        return render(request, 'eteam.html', {'form': form, 'events': events, 'current_user': current_user, 'teams': teams})


def cmember(request):
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.all()
    return render(request, 'cmember.html', {'events': events, 'current_user': current_user, 'teams': teams})
