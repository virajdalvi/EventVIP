from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, request, request, request
from django.contrib.auth.decorators import login_required
from .models import Cevent
from dashboard.models import Cmember, Ctask, Cteam
from accounts import models
from .forms import CteamForm
from dashboard.forms import CmemberForm, CtaskForm
# Create your views here.


@login_required(login_url='/accounts/login')
def dashboard(request):
    current_user = request.user
    events = Cevent.objects.filter(user_id=current_user.id)
    members = Cmember.objects.all()
    tasks = Ctask.objects.filter(user_id=current_user.id)
    teams = Cteam.objects.all()
    current_user = request.user
    counts = {
        "mcount": Cmember.objects.filter(user_id=current_user.id).count(),
        "tcount": Cteam.objects.filter(user_id=current_user.id).count(),
        "ftask": tasks.filter(status=False).count(),
        "ttask": tasks.filter(status=True).count(),
        # "totaltask": tasks.filter(status=True and False).count(),
        "dtevent": Cevent.objects.filter(user_id=current_user.id).count()

    }
    return render(request, 'dashboard.html', {'counts': counts, 'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def myevent(request):
    current_user = request.user
    # events = Cevent.objects.all()
    events = Cevent.objects.filter(
        user_id=current_user.id).values()
    return render(request, 'myevent.html', {'events': events, 'current_user': current_user})


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def selectteam(request):
    return render(request, "selectteam.html")


@login_required(login_url='/accounts/login')
def myteam(request):
    current_user = request.user
    print(current_user.id)
    events = Cevent.objects.all()
    teams = Cteam.objects.all()
    return render(request, 'myteam.html', {'events': events, 'current_user': current_user, 'teams': teams})


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def cmember(request):
    current_user = request.user
    events = Cevent.objects.all()
    # teams = Cteam.objects.filter(
    # user_id=current_user.id).values()
    teams = Cteam.objects.all()
    if request.method == 'POST':
        cmember = Cmember()
        cmember.user_id = current_user.id
        cmember.team_id = request.POST['team_id']
        cmember.first_name = request.POST['first_name']
        cmember.last_name = request.POST['last_name']
        cmember.username = request.POST['username']
        cmember.email_id = request.POST['email_id']
        cmember.phone_number = request.POST['phone_number']
        cmember.skills = request.POST['skills']
        a = teams.get(id=cmember.team_id)
        cmember.event_id = a.event_id
        b = events.get(id=cmember.event_id)
        cmember.event_name = b.event_name
        cmember.team_name = a.team_name
        cmember.save()
    return render(request, 'cmember.html', {'events': events, 'current_user': current_user, 'teams': teams})


@login_required(login_url='/accounts/login')
def mymember(request):
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    members = Cmember.objects.all()
    return render(request, 'mymember.html', {'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/login')
def dmember(request):
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    members = Cmember.objects.all()
    return render(request, 'dmember.html', {'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


def delete_member(request, pk):
    Cmember.objects.filter(id=pk).delete()
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    members = Cmember.objects.all()
    return render(request, 'dmember.html', {'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


def emember(request, pk):
    membere = get_object_or_404(Cmember, pk=pk)
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    if request.method == "POST":
        form = CmemberForm(request.POST, instance=membere)
        if form.is_valid():
            form.save()
            return redirect('mymember')
    else:
        form = CmemberForm(instance=membere)
        return render(request, 'emember.html', {'form': form, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/login')
def ctask(request):
    current_user = request.user
    events = Cevent.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    members = Cmember.objects.all()
    return render(request, 'ctask.html', {'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


def createtask(request, pk):
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    if request.method == "POST":
        ctask = Ctask()
        ctask.member_id = pk
        ctask.user_id = current_user.id
        a = members.get(id=ctask.member_id)
        ctask.event_id = a.event_id
        ctask.team_id = a.team_id
        ctask.username = a.username
        ctask.task_title = request.POST['task_title']
        ctask.task_description = request.POST['task_description']
        ctask.start_date = request.POST['start_date']
        ctask.end_date = request.POST['end_date']
        ctask.start_time = request.POST['start_time']
        ctask.end_time = request.POST['end_time']
        ctask.status = False
        ctask.first_name = a.first_name
        ctask.last_name = a.last_name
        ctask.save()
        return redirect('ctask')
    else:
        return render(request, 'createtask.html', {'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/login')
def mytasks(request):
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    return render(request, 'mytasks.html', {'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


def etask(request, pk):
    taske = get_object_or_404(Ctask, pk=pk)
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    if request.method == "POST":
        form = CtaskForm(request.POST, instance=taske)
        if form.is_valid():
            form.save()
            return redirect('mytasks')
    else:
        form = CtaskForm(instance=taske)
        return render(request, 'etask.html', {'form': form, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members, 'tasks': tasks})


def delete_task(request, pk):
    Ctask.objects.filter(id=pk).delete()
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    return render(request, 'dtask.html', {'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/login')
def dtask(request):
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    return render(request, 'dtask.html', {'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/login')
def status(request):
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    return render(request, 'status.html', {'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


def promotion(request):
    events = Cevent.objects.all()
    return render(request, 'promotion.html', {'events': events})


@login_required(login_url='/accounts/clogin')
def cdashboard(request):
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.all()
    current_user = request.user
    return render(request, 'cdashboard.html', {'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


@login_required(login_url='/accounts/clogin')
def estatus(request, pk):
    taske = get_object_or_404(Ctask, pk=pk)
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.filter(
        user_id=current_user.id).values()
    taske.status = True
    taske.save()

    return render(request, 'cdashboard.html', {'events': events, 'current_user': current_user, 'teams': teams, 'members': members, 'tasks': tasks})


@login_required(login_url='/accounts/clogin')
def completedtasks(request):
    current_user = request.user
    events = Cevent.objects.all()
    members = Cmember.objects.all()
    tasks = Ctask.objects.all()
    teams = Cteam.objects.all()
    current_user = request.user
    return render(request, 'completedtasks.html', {'tasks': tasks, 'events': events, 'current_user': current_user, 'teams': teams, 'members': members})


def clogout(request):
    auth.logout(request)
    return redirect('/')
