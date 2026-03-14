from __future__ import annotations

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.games.infrastructure.models import Games


class GameResource(resources.ModelResource):
    class Meta:
        model = Games
        fields = ("id", "name", "slug", "description", "release_year", "genre", "developer", "publisher", "active")
        import_id_fields = ("id",)


@admin.register(Games)
class GameAdmin(ImportExportModelAdmin):
    resource_classes = [GameResource]
    list_display = ("name", "release_year", "genre", "developer", "publisher", "active")
    search_fields = ("name", "slug")
    list_filter = ("genre", "developer", "release_year")
    filter_horizontal = ("consoles",)
