from django.shortcuts import render
from .models import Team
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required(login_url='/accounts/login')
def vteam(request):
    current_user = request.user
    print(current_user.id)
    teams = Team.objects.all()
    return render(request, 'viewteam.html', {'teams': teams})
