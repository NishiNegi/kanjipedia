from django.contrib import admin
from .models import Kanji

# Register your models here.

@admin.register(Kanji)
class KanjiAdmin(admin.ModelAdmin):
    list_display = ('character', 'onyomi', 'kunyomi')
    list_filter = ('grade', 'JLPT', 'strokeCount')
