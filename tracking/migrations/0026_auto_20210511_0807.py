# Generated by Django 3.1.5 on 2021-05-11 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0025_auto_20210511_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 6, 4, 8, 7, 29, 865078)),
        ),
    ]
