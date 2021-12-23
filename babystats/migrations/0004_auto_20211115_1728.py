# Generated by Django 3.2.9 on 2021-11-15 22:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('babystats', '0003_auto_20211115_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 22, 28, 48, 947272, tzinfo=utc), verbose_name='Time started'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 22, 28, 48, 947296, tzinfo=utc), verbose_name='Time ended'),
        ),
    ]
