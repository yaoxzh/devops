# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='monitorMemory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hostid', models.IntegerField(verbose_name='监控主机ID')),
                ('avai', models.CharField(verbose_name='空闲内存', max_length=20)),
                ('total', models.CharField(verbose_name='总内存', max_length=20)),
                ('ratio', models.CharField(verbose_name='使用率', max_length=20)),
                ('time', models.DateTimeField(verbose_name='时间', auto_now_add=True)),
            ],
        ),
    ]
