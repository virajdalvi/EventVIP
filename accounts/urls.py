from django.urls import path

from . import views
from dashboard.views import *

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('cregister', views.cregister, name='cregister'),
    path('clogin', views.clogin, name='clogin'),
    path('clogout', views.clogout, name='clogout'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/cdashboard', cdashboard, name='cdashboard'),
]
