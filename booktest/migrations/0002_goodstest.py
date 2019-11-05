# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsTest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.SmallIntegerField(verbose_name='商品状态', choices=[(0, '下架'), (1, '上架')], default=1)),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情')),
            ],
            options={
                'db_table': 'df_goods_test',
            },
        ),
    ]
