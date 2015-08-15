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
                ('skill_level', models.ForeignKey(related_name='char_fields', to='skills.SkillLevel', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CharFieldTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='builder.CharField')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_level', models.ForeignKey(related_name='image_fields', to='skills.SkillLevel', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageFieldTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='builder.ImageField')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_level', models.ForeignKey(related_name='text_fields', to='skills.SkillLevel', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextFieldTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2, choices=[(b'EN', b'English'), (b'RU', b'Russian'), (b'UA', b'Ukrainian')])),
                ('name', models.CharField(max_length=22)),
                ('translation_of', models.ForeignKey(related_query_name=b'translation', related_name='translations', to='builder.TextField')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='textfieldtranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='imagefieldtranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='charfieldtranslation',
            unique_together=set([('translation_of', 'language')]),
        ),
    ]
