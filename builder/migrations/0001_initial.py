# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=100)),
                ('skill', models.ForeignKey(related_name='charfield_set', to='skills.Skill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.ForeignKey(related_name='imagefield_set', to='skills.Skill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.TextField()),
                ('skill', models.ForeignKey(related_name='textfield_set', to='skills.Skill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
