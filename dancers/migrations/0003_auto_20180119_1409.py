# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0002_auto_20180119_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dancer',
            name='trainer',
        ),
        migrations.AddField(
            model_name='dancer',
            name='trainer',
            field=models.ManyToManyField(to='dancers.Trainer', verbose_name='\u0421\u0442.\u0442\u0440\u0435\u043d\u0435\u0440'),
        ),
    ]
