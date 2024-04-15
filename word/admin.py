from django.contrib import admin
from .models import Word
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Word)
class WordAdmin(ImportExportModelAdmin):
    pass 