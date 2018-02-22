# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0443\u0431',
                'verbose_name_plural': '\u041a\u043b\u0443\u0431\u044b',
            },
        ),
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numbs', models.CharField(max_length=20, verbose_name='\u2116 \u041a\u043d.')),
                ('fio', models.CharField(max_length=200, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f')),
                ('otch', models.CharField(max_length=200, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('date_birth', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('dst', models.DateTimeField(max_length=20, verbose_name='\u0414.ST')),
                ('dla', models.DateTimeField(max_length=20, verbose_name='\u0414.LA')),
                ('drank', models.DateTimeField(max_length=20, verbose_name='\u0414.\u0420\u0430\u0437\u0440\u044f\u0434', blank=True)),
                ('transl', models.CharField(max_length=50, verbose_name='\u0422\u0440\u0430\u043d\u0441\u043b\u0438\u0442')),
                ('city', models.CharField(default=b'\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0', max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('reg', models.IntegerField(default=75)),
                ('votes', models.IntegerField(default=0)),
                ('dper', models.DateTimeField(max_length=20, verbose_name='\u041f\u0435\u0440\u0435\u0445\u043e\u0434', blank=True)),
                ('partner', models.CharField(max_length=50, verbose_name='\u041f\u0430\u0440\u0442\u043d\u0435\u0440', blank=True)),
                ('wdsf', models.CharField(max_length=50, verbose_name='WDSF MIN', blank=True)),
                ('club', models.ForeignKey(verbose_name='\u041a\u043b\u0443\u0431', to='dancers.Club')),
            ],
            options={
                'verbose_name': '\u0422\u0430\u043d\u0446\u043e\u0440',
                'verbose_name_plural': '\u0422\u0430\u043d\u0446\u043e\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='La',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': 'la',
                'verbose_name_plural': 'las',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0437\u0440\u044f\u0434',
                'verbose_name_plural': '\u0420\u0430\u0437\u0440\u044f\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='St',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': 'st',
                'verbose_name_plural': 'sts',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0422\u0440\u0435\u043d\u0435\u0440',
                'verbose_name_plural': '\u0422\u0440\u0435\u043d\u0435\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='dancer',
            name='la',
            field=models.ForeignKey(verbose_name='LA', to='dancers.La'),
        ),
        migrations.AddField(
            model_name='dancer',
            name='rank',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0437\u0440\u044f\u0434', blank=True, to='dancers.Rank'),
        ),
        migrations.AddField(
            model_name='dancer',
            name='st',
            field=models.ForeignKey(verbose_name='ST', to='dancers.St'),
        ),
        migrations.AddField(
            model_name='dancer',
            name='trainer',
            field=models.ForeignKey(verbose_name='\u0422\u0440\u0435\u043d\u0435\u0440 2', blank=True, to='dancers.Trainer'),
        ),
    ]
