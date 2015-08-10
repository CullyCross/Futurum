from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from builder.models import TextField, CharField, ImageField, TextFieldTranslation, CharFieldTranslation, \
    ImageFieldTranslation

# https://github.com/s-block/django-nested-inline/issues/31

from .models import \
    Skill, SkillTranslation, \
    Reference, ReferenceTranslation, \
    Category, CategoryTranslation, \
    SkillLevel, SkillLevelTranslation

mapped_models = (
    (Reference, ReferenceTranslation),
    (Category, CategoryTranslation),
    (SkillLevel, SkillLevelTranslation)
)

for model, lang_model in mapped_models:
    class LanguageModelInlineAdmin(NestedStackedInline):
        model = lang_model

    class MainModelAdmin(NestedModelAdmin):
        inlines = LanguageModelInlineAdmin,

    try:
        admin.site.register(model, MainModelAdmin)
    except AlreadyRegistered:
        pass


class TextFieldTranslationInline(NestedStackedInline):
    model = TextFieldTranslation
    fk_name = 'translation_of'


class CharFieldTranslationInline(NestedStackedInline):
    model = CharFieldTranslation
    fk_name = 'translation_of'


class ImageFieldTranslationInline(NestedStackedInline):
    model = ImageFieldTranslation
    fk_name = 'translation_of'


class LanguageSkillInlineAdmin(NestedStackedInline):
    model = SkillTranslation
    fk_name = 'translation_of'


class TextFieldSkillInlineAdmin(NestedStackedInline):
    model = TextField
    fk_name = 'skill'
    inlines = [TextFieldTranslationInline, ]


class CharFieldSkillInlineAdmin(NestedStackedInline):
    model = CharField
    fk_name = 'skill'
    inlines = [CharFieldTranslationInline, ]


class ImageFieldSkillInlineAdmin(NestedStackedInline):
    model = ImageField
    fk_name = 'skill'
    inlines = [ImageFieldTranslationInline, ]


class SkillAdmin(NestedModelAdmin):
    model = Skill
    inlines = [LanguageSkillInlineAdmin, TextFieldSkillInlineAdmin,
               CharFieldSkillInlineAdmin, ImageFieldSkillInlineAdmin]


admin.site.register(Skill, SkillAdmin)
