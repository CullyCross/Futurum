from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import \
    TextField, TextFieldTranslation, \
    CharField, CharFieldTranslation, \
    ImageField, ImageFieldTranslation

mapped_models = (
    (TextField, TextFieldTranslation),
    (CharField, CharFieldTranslation),
    (ImageField, ImageFieldTranslation)
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
