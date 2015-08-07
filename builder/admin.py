from django.contrib import admin
from builder.models import TextField, CharField, ImageField

admin.site.register((TextField, CharField, ImageField), admin.ModelAdmin)
