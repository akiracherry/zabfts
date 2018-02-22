# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0017_auto_20180220_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atl',
            name='dancer1',
            field=models.CharField(max_length=20, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 1'),
        ),
        migrations.AlterField(
            model_name='atl',
            name='dancer2',
            field=models.CharField(max_length=20, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 2'),
        ),
    ]
