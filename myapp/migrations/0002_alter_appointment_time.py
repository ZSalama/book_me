# Generated by Django 5.0.7 on 2024-08-12 23:24

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(choices=[(datetime.time(13, 0), '1:00 PM'), (datetime.time(14, 0), '2:00 PM'), (datetime.time(15, 0), '3:00 PM'), (datetime.time(16, 0), '4:00 PM')], default=django.utils.timezone.now),
        ),
    ]
