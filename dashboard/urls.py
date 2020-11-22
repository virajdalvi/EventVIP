from django.urls import path
from django.conf.urls import url
from . import views
from dashboard.views import devent
from .views import *
from accounts.views import clogout, logout

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('cdashboard', cdashboard, name='cdashboard'),
    path('cevent', cevent, name='cevent'),
    path('myevent', myevent, name='myevent'),
    path('devent/', devent, name='devent'),
    path('cteam', cteam, name='cteam'),
    path('myteam', myteam, name='myteam'),
    path('dteam', dteam, name='dteam'),
    path('cmember', cmember, name='cmember'),
    path('mymember', mymember, name='mymember'),
    path('dmember', dmember, name='dmember'),
    path('ctask', ctask, name='ctask'),
    path('createtask/createtask', ctask, name='ctask'),
    path('mytasks', mytasks, name='mytasks'),
    path('dtask', dtask, name='dtask'),
    path('status', status, name='status'),
    path('events', promotion, name='promotion'),
    path('logout', logout, name='logout'),
    path('completedtasks', completedtasks, name='completedtasks'),
    path('clogout', clogout, name='clogout'),
    url(r'^delete_event/(?P<pk>\d+)$', delete_event, name='delete_event'),
    url(r'^delete_team/(?P<pk>\d+)$', delete_team, name='delete_team'),
    url(r'^delete_member/(?P<pk>\d+)$', delete_member, name='delete_member'),
    url(r'^eteam/(?P<pk>\d+)$', eteam, name='eteam'),
    url(r'^emember/(?P<pk>\d+)$', emember, name='emember'),
    url(r'^createtask/(?P<pk>\d+)$', createtask, name='createtask'),
    url(r'^etask/(?P<pk>\d+)$', etask, name='etask'),
    url(r'^delete_task/(?P<pk>\d+)$', delete_task, name='delete_task'),
    url(r'^estatus/(?P<pk>\d+)$', estatus, name='estatus'),



]
