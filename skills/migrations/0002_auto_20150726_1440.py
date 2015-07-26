# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('category', models.ForeignKey(related_query_name='translation', related_name='translations', to='skills.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferenceTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('reference', models.ForeignKey(related_query_name='translation', related_name='translations', to='skills.Reference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevelActionTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('skill_level_action', models.ForeignKey(related_query_name='translation', related_name='translations', to='skills.SkillLevelAction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevelTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('skill_level', models.ForeignKey(related_query_name='translation', related_name='translations', to='skills.SkillLevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('skill', models.ForeignKey(related_query_name='translation', related_name='translations', to='skills.Skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='categorylanguage',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='categorylanguage',
            name='category',
        ),
        migrations.AlterUniqueTogether(
            name='referencelanguage',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='referencelanguage',
            name='reference',
        ),
        migrations.AlterUniqueTogether(
            name='skilllanguage',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='skilllanguage',
            name='skill',
        ),
        migrations.AlterUniqueTogether(
            name='skilllevelactionlanguage',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='skilllevelactionlanguage',
            name='skill_level_action',
        ),
        migrations.AlterUniqueTogether(
            name='skilllevellanguage',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='skilllevellanguage',
            name='skill_level',
        ),
        migrations.DeleteModel(
            name='CategoryLanguage',
        ),
        migrations.DeleteModel(
            name='ReferenceLanguage',
        ),
        migrations.DeleteModel(
            name='SkillLanguage',
        ),
        migrations.DeleteModel(
            name='SkillLevelActionLanguage',
        ),
        migrations.DeleteModel(
            name='SkillLevelLanguage',
        ),
        migrations.AlterUniqueTogether(
            name='skilltranslation',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillleveltranslation',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='skilllevelactiontranslation',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='referencetranslation',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('id', 'language')]),
        ),
    ]
