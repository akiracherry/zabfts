# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0008_auto_20180119_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rank',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
