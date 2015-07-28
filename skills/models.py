from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models


# todo(CullyCross): check if it's possible to do not show
# empty line in admin panel and also choices that are used
KIDS = 'K'
FAMILY = 'F'
PERSONAL = 'M'

LANG_EN = 'EN'
LANG_RU = 'RU'
LANG_UA = 'UA'

CONTEXT = (
    (PERSONAL, 'Personal'),
    (FAMILY, 'Family'),
    (KIDS, 'Kids'),
)

LANGUAGES = (
    (LANG_EN, 'English'),
    (LANG_RU, 'Russian'),
    (LANG_UA, 'Ukrainian'),
)


class TranslatableEntityManager(models.Manager):
    def get_queryset(self):
        return super(TranslatableEntityManager, self) \
            .get_queryset().prefetch_related('translations')


class AbstractTranslatableEntity(models.Model):
    class Meta:
        abstract = True

    # Manager
    objects = TranslatableEntityManager()

    def __str__(self):

        try:
            return self.translations.get(language=LANG_EN).name
        except MultipleObjectsReturned:  # todo(CullyCross) check if it has to work this way
            return self.translations.filter(language=LANG_EN).first().name
        except ObjectDoesNotExist:
            try:
                return self.translations.first().name
            except ObjectDoesNotExist:
                return 'Untranslated yet entity'


class AbstractTranslationModel(models.Model):
    class Meta:
        abstract = True
        # fixme(CullyCross): unique_together with sub model's fields (foreign key)
        # unique_together = (('translation_of__id', 'language'), )

    language = models.CharField(max_length=2, choices=LANGUAGES)

    # Translatable fields
    name = models.CharField(max_length=22)
    description = models.TextField(default='')

    def __str__(self):
        return self.name + ' ' + str(self.language)


TM = AbstractTranslationModel
TE = AbstractTranslatableEntity


class Skill(TE):
    # Another fields
    context = models.CharField(max_length=1, choices=CONTEXT)


class SkillTranslation(TM):
    # Foreign keys
    translation_of = models.ForeignKey(Skill, related_name='translations',
                                       related_query_name='translation')


class Reference(TE):
    # Foreign keys
    skills = models.ManyToManyField(Skill, related_name='references')

    # Other fields
    email = models.EmailField()
    # picture = models.ImageField(upload_to='refs/')


class ReferenceTranslation(TM):
    # Foreign keys
    translation_of = models.ForeignKey(Reference, related_name='translations',
                                       related_query_name='translation')


class Category(TE):
    # Foreign keys
    skills = models.ManyToManyField(Skill, related_name='categories')


class CategoryTranslation(TM):
    # Foreign keys
    translation_of = models.ForeignKey(Category, related_name='translations',
                                       related_query_name='translation')


class SkillLevel(TE):
    # Foreign keys
    skill = models.ForeignKey(Skill, related_name='levels')

    # Other fields
    level = models.IntegerField()
    # picture = models.ImageField(upload_to='levels/')


class SkillLevelTranslation(TM):
    # Foreign keys
    translation_of = models.ForeignKey(SkillLevel, related_name='translations',
                                       related_query_name='translation')


class SkillLevelAction(TE):
    # Foreign keys
    skill_level = models.ForeignKey(SkillLevel, related_name='actions')


class SkillLevelActionTranslation(TM):
    # Foreign keys
    translation_of = models.ForeignKey(SkillLevelAction, related_name='translations',
                                       related_query_name='translation')
