# Generated by Django 3.1.5 on 2021-12-15 12:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracking', '0031_auto_20211028_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routed',
            name='routed_to',
        ),
        migrations.AddField(
            model_name='routed',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 1, 8, 12, 29, 49, 751411)),
        ),
    ]
