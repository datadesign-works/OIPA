# Generated by Django 2.0.6 on 2018-07-27 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0002_region_added_manually'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='added_manually',
        ),
    ]
