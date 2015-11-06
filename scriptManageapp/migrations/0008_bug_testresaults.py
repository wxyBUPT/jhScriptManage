# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0007_testimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bugDesc', models.TextField()),
                ('screenShot', models.ManyToManyField(to='scriptManageapp.TestImage')),
                ('script', models.ForeignKey(to='scriptManageapp.TestScript')),
            ],
        ),
        migrations.CreateModel(
            name='TestResaults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runDate', models.DateField()),
                ('runTime', models.TimeField()),
                ('failCount', models.IntegerField()),
                ('successCount', models.IntegerField()),
                ('bugs', models.ManyToManyField(to='scriptManageapp.Bug')),
                ('runScripts', models.ManyToManyField(to='scriptManageapp.TestScript')),
            ],
        ),
    ]
