# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('karma', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd0\xbc\xd0\xb0')),
                ('is_public', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80')),
                ('foto', models.ImageField(upload_to=b'images/%Y/%m/%d', null=True, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('date_of_birth', models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
            ],
            options={
                'db_table': 'dobro_accounts',
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0441\u0430\u0439\u0442\u0430',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0441\u0430\u0439\u0442\u0430',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
