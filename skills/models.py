from django.db import models
from Futurum import settings


class Context(models.Model):

    type = models.CharField(max_length=1, choices=(
        ('M', 'Personal'),
        ('F', 'Family'),
        ('K', 'Kids'),
    ))


class Language(models.Model):

    language = models.CharField(max_length=2, choices=(
        ('EN', 'English'),
        ('RU', 'Russian'),
        ('UA', 'Ukrainian'),
    ))


class Skill(models.Model):

    # Foreign keys
    skill_context = models.ForeignKey('Context', related_name='skills')


class SkillLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='skill_translations')
    skill = models.ForeignKey('Skill', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()


class Reference(models.Model):

    # Foreign keys
    skills = models.ManyToManyField('Skill', related_name='references')

    # Other fields
    email = models.EmailField()
    picture = models.ImageField(upload_to=settings.IMAGES_URL+'refs/')


class ReferenceLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='reference_translations')
    reference = models.ForeignKey('Reference', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()


class Category(models.Model):

    # Foreign keys
    skills = models.ManyToManyField('Skill', related_name='categories')


class CategoryLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='category_translations')
    category = models.ForeignKey('Category', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)


class SkillLevel(models.Model):

    # Foreign keys
    skill = models.ForeignKey('Skill', related_name='levels')

    # Other fields
    level = models.IntegerField()
    picture = models.ImageField(upload_to=settings.IMAGES_URL+'levels/')


class SkillLevelLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='skill_levels_translations')
    skill_level = models.ForeignKey('SkillLevel', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()


class SkillLevelAction(models.Model):

    # Foreign keys
    skill_level = models.ForeignKey('SkillLevel', related_name='actions')


class SkillLevelActionLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='skill_level_actions_translations')
    skill_level_action = models.ForeignKey('SkillLevelAction', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()
