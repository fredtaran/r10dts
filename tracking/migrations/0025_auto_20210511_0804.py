# Generated by Django 3.1.5 on 2021-05-11 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0024_auto_20210426_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 6, 7, 8, 4, 46, 52933)),
        ),
    ]