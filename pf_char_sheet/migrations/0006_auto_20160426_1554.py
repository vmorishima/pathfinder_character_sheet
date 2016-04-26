# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_char_sheet', '0005_auto_20160426_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='current_HP',
            field=models.IntegerField(default=10, verbose_name=b'Current HP'),
        ),
        migrations.AlterField(
            model_name='character',
            name='HP',
            field=models.IntegerField(default=10, verbose_name=b'Max HP'),
        ),
    ]
