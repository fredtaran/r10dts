# Generated by Django 3.1.5 on 2021-04-26 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0022_auto_20210426_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 5, 21, 10, 28, 4, 455401)),
        ),
    ]