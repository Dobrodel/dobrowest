# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dobrowest.functions


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_auto_20150417_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='foto',
            field=models.ImageField(upload_to=dobrowest.functions.get_path_to_image, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
        ),
    ]
