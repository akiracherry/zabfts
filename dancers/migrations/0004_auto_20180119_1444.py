# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0003_auto_20180119_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.AddField(
            model_name='club',
            name='ruk',
            field=models.ForeignKey(default=1, verbose_name='\u0421\u0442.\u0442\u0440\u0435\u043d\u0435\u0440', to='dancers.Trainer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dancer',
            name='trainer',
            field=models.ManyToManyField(to='dancers.Trainer', verbose_name='\u0422\u0440\u0435\u043d\u0435\u0440'),
        ),
        migrations.AddField(
            model_name='dancer',
            name='strainer',
            field=models.ForeignKey(default=2, verbose_name='\u041a\u043b\u0443\u0431', to='dancers.Ruk'),
            preserve_default=False,
        ),
    ]
