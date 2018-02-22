# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancers', '0012_category_news_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
                ('dancer', models.ForeignKey(verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440 2', to='dancers.Dancer', max_length=300)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0430\u043d\u0446\u043e\u0440',
                'verbose_name_plural': '\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0442\u0430\u043d\u0446\u043e\u0440\u044b',
            },
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': '\u0422\u0443\u0440\u043d\u0438\u0440', 'verbose_name_plural': '\u0422\u0443\u0440\u043d\u0438\u0440\u044b'},
        ),
        migrations.AddField(
            model_name='tour',
            name='doptext',
            field=models.TextField(verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='atl',
            name='tour',
            field=models.ForeignKey(verbose_name='\u0422\u0443\u0440\u043d\u0438\u0440', to='dancers.Tour'),
        ),
    ]
