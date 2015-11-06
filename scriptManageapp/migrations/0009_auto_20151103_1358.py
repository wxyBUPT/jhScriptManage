# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptManageapp', '0008_bug_testresaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='email',
            field=models.CharField(max_length=30, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='project',
            name='proDesc',
            field=models.TextField(verbose_name='\u9879\u76ee\u63cf\u8ff0'),
        ),
    ]
