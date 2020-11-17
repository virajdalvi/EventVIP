from django.db import models


class Cevent(models.Model):
    user_id = models.IntegerField()
    event_name = models.CharField(max_length=500)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_type = models.CharField(max_length=100)
    event_category = models.CharField(max_length=100)
    event_website = models.URLField()
    event_description = models.TextField(max_length=10000)


class Cteam(models.Model):
    user_id = models.IntegerField()
    event_id = models.IntegerField()
    team_name = models.CharField(max_length=500)
    team_ptask = models.CharField(max_length=1000)
    team_description = models.TextField(max_length=10000)
