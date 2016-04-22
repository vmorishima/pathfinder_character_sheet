# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.SmallIntegerField(default=1)),
                ('character_class', models.CharField(max_length=50)),
                ('alignment', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=75)),
            ],
        ),
    ]
