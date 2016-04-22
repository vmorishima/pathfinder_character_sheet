# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_char_sheet', '0002_auto_20160421_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='BAB',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='CHA',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='CON',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='DEX',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='FORT',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='HP',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='INT',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='REFLEX',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='STR',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='WILL',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='WIS',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='size',
            field=models.CharField(default=b'm', max_length=1, choices=[(b't', b'Tiny'), (b'h', b'Huge'), (b'c', b'Colossal'), (b'l', b'Large'), (b'g', b'Gargantuan'), (b'd', b'Diminutive'), (b's', b'Small'), (b'f', b'Fine'), (b'm', b'Medium')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
