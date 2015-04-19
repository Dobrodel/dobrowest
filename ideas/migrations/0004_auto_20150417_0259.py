# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20150415_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideas',
            name='published',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='type',
            field=models.CharField(default=b'T', help_text=b'\xd0\x92\xd1\x8b\xd0\xb1\xd0\xb8\xd1\x80\xd0\xb8\xd1\x82\xd0\xb5 \xd1\x82\xd0\xb8\xd0\xbf \xd0\x92\xd0\xb0\xd1\x88\xd0\xb5\xd0\xb9 \xd0\xb8\xd0\xb4\xd0\xb5\xd0\xb8', max_length=1, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb8\xd0\xb4\xd0\xb5\xd0\xb8', choices=[(1, b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0'), (2, b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd1\x8f'), (3, b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9')]),
        ),
    ]