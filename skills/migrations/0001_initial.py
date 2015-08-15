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
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default=b'')),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default=b'')),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.Reference')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=1, choices=[(b'M', b'Personal'), (b'F', b'Family'), (b'K', b'Kids')])),
                ('contributors', models.ManyToManyField(related_name='contributed_to', to=settings.AUTH_USER_MODEL, blank=True)),
                ('owner', models.ForeignKey(related_name='created_skills', to=settings.AUTH_USER_MODEL, db_constraint=False)),
                ('parent_skills', models.ManyToManyField(related_name='parent_skills_rel_+', to='skills.Skill', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('skill', models.ForeignKey(related_name='levels', to='skills.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillLevelTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default=b'')),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.SkillLevel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default=b'')),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='skilltranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillleveltranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='skilllevel',
            unique_together=set([('skill', 'level')]),
        ),
        migrations.AlterUniqueTogether(
            name='referencetranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
        migrations.AddField(
            model_name='reference',
            name='skills',
            field=models.ManyToManyField(related_name='references', to='skills.Skill'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
        migrations.AddField(
            model_name='category',
            name='skills',
            field=models.ManyToManyField(related_name='categories', to='skills.Skill'),
            preserve_default=True,
        ),
    ]
