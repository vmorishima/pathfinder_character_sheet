# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_char_sheet', '0006_auto_20160426_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='XP',
            field=models.IntegerField(default=0, verbose_name=b'Current HP'),
        ),
    ]
