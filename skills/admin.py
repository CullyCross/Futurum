from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import \
    Skill, SkillTranslation, \
    Reference, ReferenceTranslation, \
    Category, CategoryTranslation, \
    SkillLevel, SkillLevelTranslation

mapped_models = (
    (Skill, SkillTranslation),
    (Reference, ReferenceTranslation),
    (Category, CategoryTranslation),
    (SkillLevel, SkillLevelTranslation)
)

for model, lang_model in mapped_models:
    class LanguageModelInlineAdmin(admin.TabularInline):
        model = lang_model

    class MainModelAdmin(admin.ModelAdmin):
        inlines = LanguageModelInlineAdmin,

    try:
        admin.site.register(model, MainModelAdmin)
    except AlreadyRegistered:
        pass
