# Generated by Django 3.1.5 on 2021-02-22 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0010_auto_20210208_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(choices=[('Incoming-Ext', 'Incoming-Ext'), ('Outgoing-Ext', 'Outgoing-Ext'), ('Incoming-Int', 'Incoming-Int'), ('Outgoing-Int', 'Outgoing-Int')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 3, 9, 10, 9, 16, 738721)),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
