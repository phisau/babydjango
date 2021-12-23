# Generated by Django 3.2.9 on 2021-11-15 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shit', models.BooleanField(verbose_name='Contains shit')),
                ('mood', models.IntegerField(default=0)),
                ('time_from', models.DateTimeField(verbose_name='Time started')),
                ('time_to', models.DateTimeField(verbose_name='Time ended')),
                ('actiontype_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babystats.category')),
            ],
        ),
    ]
