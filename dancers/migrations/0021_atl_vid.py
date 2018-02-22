# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0020_auto_20180220_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='atl',
            name='vid',
            field=models.CharField(default=b'\xd0\x9e\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8b\xd0\xb9 \xd1\x82\xd1\x83\xd1\x80\xd0\xbd\xd0\xb8\xd1\x80', max_length=30, verbose_name='\u0412\u0438\u0434'),
        ),
    ]
