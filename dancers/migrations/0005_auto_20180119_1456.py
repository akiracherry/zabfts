# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0004_auto_20180119_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='ruk',
            field=models.ForeignKey(verbose_name='\u0421\u0442.\u0442\u0440\u0435\u043d\u0435\u0440', to='dancers.Ruk'),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='strainer',
            field=models.ForeignKey(verbose_name='\u0421\u0442.\u0442\u0440\u0435\u043d\u0435\u0440', to='dancers.Ruk'),
        ),
    ]
