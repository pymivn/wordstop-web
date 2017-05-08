from django.contrib import admin

from .models import Word, Book


class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'frequency', 'example', 'book')


admin.site.register(Book)
admin.site.register(Word, WordAdmin)
