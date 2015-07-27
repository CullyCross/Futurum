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
                ('category', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('picture', models.ImageField(upload_to=b'/images/refs/')),
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
                ('reference', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.Reference')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=1, choices=[(b'M', b'Personal'), (b'F', b'Family'), (b'K', b'Kids')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('picture', models.ImageField(upload_to=b'/images/levels/')),
                ('skill', models.ForeignKey(related_name='levels', to='skills.Skill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillLevelAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_level', models.ForeignKey(related_name='actions', to='skills.SkillLevel')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillLevelActionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('description', models.TextField(default=b'')),
                ('skill_level_action', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.SkillLevelAction')),
            ],
            options={
                'abstract': False,
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
                ('skill_level', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.SkillLevel')),
            ],
            options={
                'abstract': False,
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
                ('skill', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='skills.Skill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
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
            name='skill',
            unique_together=set([('id', 'context')]),
        ),
        migrations.AlterUniqueTogether(
            name='referencetranslation',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AddField(
            model_name='reference',
            name='skills',
            field=models.ManyToManyField(related_name='references', to='skills.Skill'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('id', 'language')]),
        ),
        migrations.AddField(
            model_name='category',
            name='skills',
            field=models.ManyToManyField(related_name='categories', to='skills.Skill'),
            preserve_default=True,
        ),
    ]
