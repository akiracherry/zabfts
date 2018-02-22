# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0019_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atl',
            name='tour',
        ),
        migrations.AddField(
            model_name='atl',
            name='group',
            field=models.ManyToManyField(to='dancers.Group', verbose_name='\u0422\u0443\u0440\u043d\u0438\u0440'),
        ),
        migrations.AddField(
            model_name='group',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c'),
        ),
    ]
