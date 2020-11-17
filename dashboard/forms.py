from django import forms
from .models import *


class CteamForm(forms.ModelForm):
    class Meta:
        model = Cteam
        fields = ('team_name', 'team_ptask', 'team_description')
