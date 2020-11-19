from django.urls import path
from django.conf.urls import url
from . import views
from dashboard.views import devent
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('cevent', cevent, name='cevent'),
    path('myevent', myevent, name='myevent'),
    path('devent/', devent, name='devent'),
    path('cteam', cteam, name='cteam'),
    path('myteam', myteam, name='myteam'),
    path('dteam', dteam, name='dteam'),
    path('cmember', cmember, name='cmember'),
    url(r'^delete_event/(?P<pk>\d+)$', delete_event, name='delete_event'),
    url(r'^delete_team/(?P<pk>\d+)$', delete_team, name='delete_team'),
    url(r'^eteam/(?P<pk>\d+)$', eteam, name='eteam'),



]
