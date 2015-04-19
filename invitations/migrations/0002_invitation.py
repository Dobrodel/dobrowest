# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150415_1228'),
        ('invitations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(help_text='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 email \u0430\u0434\u0440\u0435\u0441\u0430\u0442\u0430', unique=True, max_length=254, verbose_name='E-mail \u0430\u0434\u0440\u0435\u0441\u0430\u0442\u0430', validators=[django.core.validators.EmailValidator()])),
                ('accepted', models.BooleanField(default=False, verbose_name='\u041a\u043e\u0434 \u043f\u0440\u0438\u043d\u044f\u0442')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('key', models.CharField(unique=True, max_length=64, verbose_name='\u041a\u043e\u0434 \u043f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u044f')),
                ('sent', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('invited', models.IntegerField(default=0, null=True, verbose_name='\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u043d\u044b\u0439', blank=True)),
                ('user', models.ForeignKey(verbose_name='\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0430\u044e\u0449\u0438\u0439', to='accounts.CustomUser')),
            ],
            options={
                'db_table': 'dobro_invitations',
                'verbose_name': '\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u044f',
            },
        ),
    ]
