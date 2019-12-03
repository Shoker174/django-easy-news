# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-21 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creation date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short',
            field=models.TextField(blank=True, default=b'', verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=tinymce.models.HTMLField(blank=True, default=b'', verbose_name='main content'),
        ),
    ]
