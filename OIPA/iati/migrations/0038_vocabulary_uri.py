# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati_codelists', '0005_auto_20160602_1644'),
        ('iati', '0037_transaction-humanitarian'),
    ]

    operations = [
        migrations.AddField(
            model_name='planneddisbursementprovider',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.OrganisationType'),
        ),
        migrations.AddField(
            model_name='planneddisbursementreceiver',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.OrganisationType'),
        ),
        migrations.AddField(
            model_name='transactionprovider',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.OrganisationType'),
        ),
        migrations.AddField(
            model_name='transactionreceiver',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_codelists.OrganisationType'),
        ),
        migrations.AddField(
            model_name='transactionrecipientregion',
            name='vocabulary_uri',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactionsector',
            name='vocabulary_uri',
            field=models.URLField(blank=True, null=True),
        ),
    ]
