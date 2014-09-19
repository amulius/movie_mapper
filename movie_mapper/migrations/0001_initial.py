# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=120)),
                ('searched', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('movie_id', models.CharField(max_length=10)),
                ('searched', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(related_name=b'movies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location',
            name='movies',
            field=models.ManyToManyField(related_name=b'locations', to='movie_mapper.Movie'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ManyToManyField(related_name=b'locations', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
