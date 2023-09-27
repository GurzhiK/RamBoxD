from django.contrib import admin
from django.utils.html import mark_safe
from .models import Film, Genre, Language, Country


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'get_image')
    # Search by film id and title
    search_fields = ('id', 'title')

    def get_image(self, obj):
        if obj.poster:
            return mark_safe(f"<img src='{obj.poster.url}' width=50>")

    get_image.short_description = 'Poster'


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
