# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0014_tour_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atl',
            name='dancer',
        ),
        migrations.AddField(
            model_name='atl',
            name='dancer1',
            field=models.TextField(default=1, max_length=300, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atl',
            name='dancer2',
            field=models.TextField(default=1, max_length=300, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 2'),
            preserve_default=False,
        ),
    ]
