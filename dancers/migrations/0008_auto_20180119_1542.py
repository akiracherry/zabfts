# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0007_auto_20180119_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=200, verbose_name='\u041a\u043b\u0443\u0431'),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='reg',
            field=models.IntegerField(default=75, verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='rank',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u0420\u0430\u0437\u0440\u044f\u0434'),
        ),
    ]
