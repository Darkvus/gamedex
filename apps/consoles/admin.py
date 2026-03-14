from __future__ import annotations

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.consoles.infrastructure.models import Consoles


class ConsoleResource(resources.ModelResource):
    class Meta:
        model = Consoles
        fields = ("id", "name", "manufacturer", "release_year", "generation", "type", "active")
        import_id_fields = ("id",)


@admin.register(Consoles)
class ConsoleAdmin(ImportExportModelAdmin):
    resource_classes = [ConsoleResource]
    list_display = ("name", "manufacturer", "release_year", "generation", "type", "active")
    search_fields = ("name", "manufacturer")
    list_filter = ("type", "generation")
