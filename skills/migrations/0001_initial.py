# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('category', models.ForeignKey(to='skills.Category', related_name='languages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='F:/images/refs/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferenceLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('reference', models.ForeignKey(to='skills.Reference', related_name='languages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('context', models.CharField(max_length=1, unique=True, choices=[('M', 'Personal'), ('F', 'Family'), ('K', 'Kids')])),
            ],
        ),
        migrations.CreateModel(
            name='SkillLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('skill', models.ForeignKey(to='skills.Skill', related_name='languages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('picture', models.ImageField(upload_to='F:/images/levels/')),
                ('skill', models.ForeignKey(to='skills.Skill', related_name='levels')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevelAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('skill_level', models.ForeignKey(to='skills.SkillLevel', related_name='actions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevelActionLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('skill_level_action', models.ForeignKey(to='skills.SkillLevelAction', related_name='languages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillLevelLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=2, unique=True, choices=[('EN', 'English'), ('RU', 'Russian'), ('UA', 'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default='')),
                ('skill_level', models.ForeignKey(to='skills.SkillLevel', related_name='languages')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='skill',
            unique_together=set([('id', 'context')]),
        ),
        migrations.AddField(
            model_name='reference',
            name='skills',
            field=models.ManyToManyField(to='skills.Skill', related_name='references'),
        ),
        migrations.AddField(
            model_name='category',
            name='skills',
            field=models.ManyToManyField(to='skills.Skill', related_name='categories'),
        ),
        migrations.AlterUniqueTogether(
            name='skilllevellanguage',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='skilllevelactionlanguage',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='skilllanguage',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='referencelanguage',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorylanguage',
            unique_together=set([('id', 'language')]),
        ),
    ]
