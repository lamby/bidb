# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 13:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('binary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_binaries', to='packages.Binary')),
            ],
            options={
                'ordering': ('binary__name',),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Buildinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha1', models.CharField(max_length=40, unique=True)),
                ('version', models.CharField(max_length=200)),
                ('build_path', models.CharField(max_length=512)),
                ('raw_text', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('architecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildinfos', to='packages.Architecture')),
                ('build_architecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildinfos_build', to='packages.Architecture')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildinfos', to='packages.Source')),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Checksum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('checksum_md5', models.CharField(max_length=100)),
                ('checksum_sha1', models.CharField(max_length=100)),
                ('checksum_sha256', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('binary', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checksum', to='buildinfo.Binary')),
                ('buildinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checksums', to='buildinfo.Buildinfo')),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='InstalledBuildDepends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=200)),
                ('binary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build_depends', to='packages.Binary')),
                ('buildinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='installed_build_depends', to='buildinfo.Buildinfo')),
            ],
            options={
                'ordering': ('binary__name',),
                'get_latest_by': 'created',
            },
        ),
        migrations.AddField(
            model_name='binary',
            name='buildinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='binaries', to='buildinfo.Buildinfo'),
        ),
        migrations.AlterUniqueTogether(
            name='installedbuilddepends',
            unique_together=set([('buildinfo', 'binary')]),
        ),
        migrations.AlterUniqueTogether(
            name='checksum',
            unique_together=set([('buildinfo', 'filename')]),
        ),
        migrations.AlterUniqueTogether(
            name='binary',
            unique_together=set([('buildinfo', 'binary')]),
        ),
    ]
