from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import models
from skills.models import LANGUAGES, TranslatableEntityManager, LANG_EN, SkillLevel


class AbstractTranslatableField(models.Model):
    class Meta:
        abstract = True

    # Manager
    objects = TranslatableEntityManager()

    # Foreign keys
    skill_level = models.ForeignKey(SkillLevel, related_name='%(class)s_set')

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


class AbstractTranslationFieldModel(models.Model):
    class Meta:
        abstract = True

    language = models.CharField(max_length=2, choices=LANGUAGES)

    # Translatable fields
    name = models.CharField(max_length=22)

    def __str__(self):
        return self.name + ' ' + str(self.language)


TF = AbstractTranslatableField
TFM = AbstractTranslationFieldModel

class TextField(TF):
    pass


class TextFieldTranslation(TFM):
    # Foreign keys
    translation_of = models.ForeignKey(TextField, related_name='translations',
                                       related_query_name='translation')


class CharField(TF):
    pass


class CharFieldTranslation(TFM):
    # Foreign keys
    translation_of = models.ForeignKey(CharField, related_name='translations',
                                       related_query_name='translation')


class ImageField(TF):
    pass


class ImageFieldTranslation(TFM):
    # Foreign keys
    translation_of = models.ForeignKey(ImageField, related_name='translations',
                                       related_query_name='translation')

    # Other fields
    # data = models.ImageField()
