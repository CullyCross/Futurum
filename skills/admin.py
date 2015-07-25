# from django.contrib import admin
# from django.contrib.admin.sites import AlreadyRegistered
#
# from .models import \
#     Skill, SkillLanguage, \
#     Reference, ReferenceLanguage, \
#     Category, CategoryLanguage, \
#     SkillLevel, SkillLevelLanguage, \
#     SkillLevelAction, SkillLevelActionLanguage
#
# mapped_models = (
#     (Skill, SkillLanguage),
#     (Reference, ReferenceLanguage),
#     (Category, CategoryLanguage),
#     (SkillLevel, SkillLevelLanguage),
#     (SkillLevelAction, SkillLevelActionLanguage)
# )
#
# for model, lang_model in mapped_models:
#     class LanguageModelInlineAdmin(admin.TabularInline):
#         model = lang_model
#
#     class MainModelAdmin(admin.ModelAdmin):
#         inlines = LanguageModelInlineAdmin,
#
#     try:
#         admin.site.register(model, MainModelAdmin)
#     except AlreadyRegistered:
#         pass
#
# admin.site.register((Language, Context))
