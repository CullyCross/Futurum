import os
from django.db import models
from Futurum import settings
from Futurum.settings import IMAGES_ROOT


class Context(models.Model):

    # todo(CullyCross): check if it's possible to do not show empty line in admin panel and also choices that are used
    type = models.CharField(max_length=1, choices=(
        ('M', 'Personal'),
        ('F', 'Family'),
        ('K', 'Kids'),
    ), unique=True)

    def __str__(self):
        return self.get_type_display()


class Language(models.Model):

    language = models.CharField(max_length=2, choices=(
        ('EN', 'English'),
        ('RU', 'Russian'),
        ('UA', 'Ukrainian'),
    ), unique=True)

    def __str__(self):
        return self.get_language_display()


class Skill(models.Model):

    # Foreign keys
    skill_context = models.ForeignKey('Context', related_name='skills')

    # todo(CullyCross): later customize admin panel with translations inside same for all translations
    # def __str__(self):
    #     language = Language.objects.filter(language='EN')
    #
    #     objects = self.languages
    #
    #     if objects is not None:
    #         name = objects.filter(language=language).first().name
    #         if not name:
    #             name = objects.first()
    #         return name
    #     else:
    #         return 'Skill'

class SkillLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='skill_translations')
    skill = models.ForeignKey('Skill', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()

    def __str__(self):
        return self.name + ' ' + str(self.language)


class Reference(models.Model):

    # Foreign keys
    skills = models.ManyToManyField('Skill', related_name='references')

    # Other fields
    email = models.EmailField()
    picture = models.ImageField(upload_to=os.path.join(IMAGES_ROOT, 'refs/'))


class ReferenceLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='reference_translations')
    reference = models.ForeignKey('Reference', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()

    def __str__(self):
        return self.name + ' ' + str(self.language)


class Category(models.Model):

    # Foreign keys
    skills = models.ManyToManyField('Skill', related_name='categories')


class CategoryLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='category_translations')
    category = models.ForeignKey('Category', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)

    def __str__(self):
        return self.name + ' ' + str(self.language)


class SkillLevel(models.Model):

    # Foreign keys
    skill = models.ForeignKey('Skill', related_name='levels')

    # Other fields
    level = models.IntegerField()
    picture = models.ImageField(upload_to=os.path.join(IMAGES_ROOT, 'levels/'))


class SkillLevelLanguage(models.Model):

    # Foreign keys
    language = models.ForeignKey('Language', related_name='skill_levels_translations')
    skill_level = models.ForeignKey('SkillLevel', related_name='languages')

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField()

    def __str__(self):
        return self.name + ' ' + str(self.language)


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

    def __str__(self):
        return self.name + ' ' + str(self.language)

