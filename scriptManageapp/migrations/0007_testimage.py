# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0006_testscript_testpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images/')),
                ('name', models.CharField(max_length=30)),
                ('testScript', models.ForeignKey(to='scriptManageapp.TestScript')),
            ],
        ),
    ]
