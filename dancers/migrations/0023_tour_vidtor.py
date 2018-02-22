# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0022_auto_20180221_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='vidtor',
            field=models.CharField(default=1, max_length=300, verbose_name='\u0412\u0438\u0434 \u0442\u0443\u0440\u043d\u0438\u0440\u0430'),
            preserve_default=False,
        ),
    ]
