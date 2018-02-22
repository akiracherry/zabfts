# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0023_tour_vidtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='reg',
            field=models.CharField(default=1, max_length=300, verbose_name='\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u0430 \u0434\u043e:'),
            preserve_default=False,
        ),
    ]
