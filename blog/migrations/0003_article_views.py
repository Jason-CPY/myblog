# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
