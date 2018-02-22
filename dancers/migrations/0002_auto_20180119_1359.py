# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='date_birth',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='dla',
            field=models.DateField(max_length=20, verbose_name='\u0414.LA'),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='dper',
            field=models.DateField(max_length=20, verbose_name='\u041f\u0435\u0440\u0435\u0445\u043e\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='drank',
            field=models.DateField(max_length=20, verbose_name='\u0414.\u0420\u0430\u0437\u0440\u044f\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='dst',
            field=models.DateField(max_length=20, verbose_name='\u0414.ST'),
        ),
    ]
