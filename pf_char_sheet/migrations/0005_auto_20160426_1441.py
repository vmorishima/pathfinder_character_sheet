# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf_char_sheet', '0004_auto_20160425_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='knowledge_local',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Local)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='BAB',
            field=models.IntegerField(default=0, verbose_name=b'Base Attack Bonus'),
        ),
        migrations.AlterField(
            model_name='character',
            name='FORT',
            field=models.IntegerField(default=0, verbose_name=b'Base Fortitude'),
        ),
        migrations.AlterField(
            model_name='character',
            name='REFLEX',
            field=models.IntegerField(default=0, verbose_name=b'Base Reflex'),
        ),
        migrations.AlterField(
            model_name='character',
            name='WILL',
            field=models.IntegerField(default=0, verbose_name=b'Base Will'),
        ),
        migrations.AlterField(
            model_name='character',
            name='base_AC',
            field=models.IntegerField(default=0, verbose_name=b'Armor Bonuses'),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.CharField(max_length=50, verbose_name=b'Class'),
        ),
        migrations.AlterField(
            model_name='character',
            name='disable_device',
            field=models.IntegerField(default=0, verbose_name=b'Disable Device'),
        ),
        migrations.AlterField(
            model_name='character',
            name='escape_artist',
            field=models.IntegerField(default=0, verbose_name=b'Escape Artist'),
        ),
        migrations.AlterField(
            model_name='character',
            name='handle_animal',
            field=models.IntegerField(default=0, verbose_name=b'Handle Animal'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_arcana',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Arcana)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_dungeoneering',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Dungeoneering)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_engineering',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Engineering)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_geography',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Geography)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_history',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (History)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_nature',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Nature)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_nobility',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Nobility)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_planes',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Planes)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='knowledge_religion',
            field=models.IntegerField(default=0, verbose_name=b'Knowledge (Religion)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='sense_motive',
            field=models.IntegerField(default=0, verbose_name=b'Sense Motive'),
        ),
        migrations.AlterField(
            model_name='character',
            name='sleight_of_hand',
            field=models.IntegerField(default=0, verbose_name=b'Sleight of Hand'),
        ),
        migrations.AlterField(
            model_name='character',
            name='use_magic_device',
            field=models.IntegerField(default=0, verbose_name=b'Use Magic Device'),
        ),
    ]
