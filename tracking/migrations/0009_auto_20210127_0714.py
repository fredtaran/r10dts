# Generated by Django 3.1.5 on 2021-01-27 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0008_auto_20210119_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 2, 11, 7, 14, 30, 904228)),
        ),
    ]
