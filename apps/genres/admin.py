from __future__ import annotations

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.genres.infrastructure.models import Genres


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genres
        fields = ("id", "name", "description", "active")
        import_id_fields = ("id",)


@admin.register(Genres)
class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]
    list_display = ("name", "active")
    search_fields = ("name",)
