# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_invitations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitations',
            name='invited',
            field=models.IntegerField(default=0, verbose_name='\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u043d\u044b\u0439', blank=True),
        ),
    ]
