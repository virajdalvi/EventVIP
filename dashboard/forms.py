from django import forms
from .models import *


class CteamForm(forms.ModelForm):
    class Meta:
        model = Cteam
        fields = ('team_name', 'team_ptask', 'team_description')


class CmemberForm(forms.ModelForm):
    class Meta:
        model = Cmember
        fields = ('event_name', 'team_name', 'first_name',
                  'last_name', 'email_id', 'phone_number', 'skills')


class CtaskForm(forms.ModelForm):
    class Meta:
        model = Ctask
        fields = ('task_title', 'task_description',
                  'start_date', 'end_date', 'start_time', 'end_time')
