# Generated by Django 3.1.5 on 2021-10-28 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0030_auto_20211012_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carboncopy',
            name='doc_code',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 11, 21, 10, 31, 12, 755819)),
        ),
    ]
