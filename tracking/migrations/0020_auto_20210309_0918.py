# Generated by Django 3.1.5 on 2021-03-09 09:18

import datetime
from django.db import migrations, models
import tracking.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0019_auto_20210309_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='outgoing',
            name='attach_file',
            field=models.FileField(default=0, max_length=500, upload_to=tracking.models.attach_file),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2021, 3, 28, 9, 18, 43, 536775)),
        ),
        migrations.AlterField(
            model_name='document',
            name='pdf_file',
            field=models.FileField(max_length=500, upload_to=tracking.models.pdf_file_name),
        ),
        migrations.AlterField(
            model_name='document',
            name='send_file',
            field=models.FileField(max_length=500, upload_to=tracking.models.approved_file_name),
        ),
        migrations.AlterField(
            model_name='routed',
            name='attach_file',
            field=models.FileField(max_length=500, upload_to=tracking.models.attach_file_name),
        ),
    ]