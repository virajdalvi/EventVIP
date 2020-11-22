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


class Cmember(models.Model):
    username = models.CharField(max_length=100, default=0)
    user_id = models.IntegerField()
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=1000, default=0)
    team_id = models.IntegerField()
    team_name = models.CharField(max_length=1000, default=0)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email_id = models.EmailField(default=0, max_length=254)
    phone_number = models.CharField(max_length=13)
    skills = models.TextField(max_length=10000)


class Ctask(models.Model):
    username = models.CharField(max_length=100, default=0)
    user_id = models.IntegerField()
    event_id = models.IntegerField()
    team_id = models.IntegerField()
    member_id = models.IntegerField()
    first_name = models.CharField(max_length=500, default=0)
    last_name = models.CharField(max_length=500, default=0)
    task_title = models.CharField(max_length=1000)
    task_description = models.CharField(max_length=10000)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)
