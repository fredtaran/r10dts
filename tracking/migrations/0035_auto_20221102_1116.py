# Generated by Django 3.1.5 on 2022-11-02 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0034_auto_20211215_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carboncopy',
            options={'ordering': ('-date_rcv',)},
        ),
        migrations.AddField(
            model_name='document',
            name='confidential',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 11, 26, 11, 16, 49, 930497)),
        ),
    ]
