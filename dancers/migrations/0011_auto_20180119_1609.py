# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0010_auto_20180119_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='rank',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0437\u0440\u044f\u0434', blank=True, to='dancers.Rank', null=True),
        ),
    ]
