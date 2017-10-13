# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('status', 'created_date'),
            },
        ),
        migrations.DeleteModel(
            name='Update_Form',
        ),
    ]
