# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_mapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='place',
            field=models.CharField(unique=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
