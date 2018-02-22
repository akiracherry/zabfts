# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0009_auto_20180119_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='dla',
            field=models.DateField(max_length=20, null=True, verbose_name='\u0414.LA'),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='dper',
            field=models.DateField(max_length=20, null=True, verbose_name='\u041f\u0435\u0440\u0435\u0445\u043e\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='drank',
            field=models.DateField(max_length=20, null=True, verbose_name='\u0414.\u0420\u0430\u0437\u0440\u044f\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='dst',
            field=models.DateField(max_length=20, null=True, verbose_name='\u0414.ST'),
        ),
    ]
