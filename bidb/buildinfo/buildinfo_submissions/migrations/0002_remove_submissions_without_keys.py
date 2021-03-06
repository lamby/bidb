# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 20:30
from __future__ import unicode_literals

from django.db import migrations

def forwards(apps, schema_editor):
    if not schema_editor.connection.alias == 'default':
        return

    Submission = apps.get_model('buildinfo_submissions', 'Submission')

    Submission.objects.filter(uid='').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('buildinfo_submissions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
