# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_char_sheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='alignment',
            field=models.CharField(max_length=2, choices=[(b'LG', b'Lawful Good'), (b'NG', b'Neutral Good'), (b'CG', b'Chaotic Good'), (b'LN', b'Lawful Neutral'), (b'N', b'True Neutral'), (b'CN', b'Chaotic Neutral'), (b'LE', b'Lawful Evil'), (b'NE', b'Neutral Evil'), (b'CE', b'Chaotic Evil')]),
        ),
    ]
