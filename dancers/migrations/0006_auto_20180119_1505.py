# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0005_auto_20180119_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dancer',
            name='votes',
        ),
        migrations.AlterField(
            model_name='rank',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
