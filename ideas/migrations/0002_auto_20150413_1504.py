# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='uservoices',
            table='dobro_uservoices',
        ),
    ]
