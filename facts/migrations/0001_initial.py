# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('text', models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('source_url', models.URLField(default=b'/', verbose_name=b'\xd0\x98\xd1\x81\xd1\x82\xd0\xbe\xd1\x87\xd0\xbd\xd0\xb8\xd0\xba', blank=True)),
                ('foto', models.ImageField(upload_to=b'', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
            ],
            options={
                'db_table': 'dobro_facts',
                'verbose_name': '\u0413\u043e\u043b\u044b\u0435 \u0444\u0430\u043a\u0442\u044b',
                'verbose_name_plural': '\u0413\u043e\u043b\u044b\u0435 \u0444\u0430\u043a\u0442\u044b',
            },
        ),
    ]
