# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-11 19:41
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]