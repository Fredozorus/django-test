# Generated by Django 3.2.5 on 2024-09-24 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_busshift_busstop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busshift',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='busshift',
            name='departure_time',
        ),
    ]
