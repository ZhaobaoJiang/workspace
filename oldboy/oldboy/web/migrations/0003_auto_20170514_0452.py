# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-14 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170514_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
