from __future__ import annotations

import os

import tablib
from django.contrib import admin, messages
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin

from apps.consoles.infrastructure.models import Consoles

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "import", "consoles.json")


class ConsoleResource(resources.ModelResource):
    class Meta:
        model = Consoles
        fields = ("id", "name", "name_en", "name_es", "manufacturer", "release_year", "generation", "type", "active")
        import_id_fields = ("name_en",)


def load_consoles_fixture(modeladmin, request, queryset):
    with open(FIXTURE_PATH) as f:
        dataset = tablib.Dataset().load(f.read())
    result = ConsoleResource().import_data(dataset, dry_run=False, raise_errors=True)
    messages.success(request, f"Consoles fixture loaded: {result.totals}")


load_consoles_fixture.short_description = "Load consoles from fixture"


@admin.register(Consoles)
class ConsoleAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_classes = [ConsoleResource]
    list_display = ("name", "manufacturer", "release_year", "generation", "type", "active")
    search_fields = ("name", "manufacturer")
    list_filter = ("type", "generation")
    actions = [load_consoles_fixture]
