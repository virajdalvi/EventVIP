# Generated by Django 3.0.5 on 2020-11-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_ctask'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctask',
            name='first_name',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='ctask',
            name='last_name',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
