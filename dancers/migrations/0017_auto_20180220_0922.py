# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0016_auto_20180220_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='atl',
            name='email',
            field=models.TextField(default=1, max_length=50, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atl',
            name='dancer1',
            field=models.TextField(max_length=10, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 1'),
        ),
        migrations.AlterField(
            model_name='atl',
            name='dancer2',
            field=models.TextField(max_length=10, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 2'),
        ),
    ]
