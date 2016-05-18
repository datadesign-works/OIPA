# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0032_auto_20160426_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionprovider',
            name='primary_name',
            field=models.CharField(blank=True, db_index=True, default=b'', max_length=250),
        ),
        migrations.AddField(
            model_name='transactionreceiver',
            name='primary_name',
            field=models.CharField(blank=True, db_index=True, default=b'', max_length=250),
        ),
    ]
