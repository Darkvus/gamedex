from __future__ import annotations

import os

import tablib
from django.contrib import admin, messages
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin

from apps.genres.infrastructure.models import Genres

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "import", "genres.json")


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genres
        fields = ("id", "name", "name_en", "name_es", "description", "description_en", "description_es", "active")
        import_id_fields = ("name_en",)


def load_genres_fixture(modeladmin, request, queryset):
    with open(FIXTURE_PATH) as f:
        dataset = tablib.Dataset().load(f.read())
    result = GenreResource().import_data(dataset, dry_run=False, raise_errors=True)
    messages.success(request, f"Genres fixture loaded: {result.totals}")


load_genres_fixture.short_description = "Load genres from fixture"


@admin.register(Genres)
class GenreAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_classes = [GenreResource]
    list_display = ("name", "active")
    search_fields = ("name",)
    actions = [load_genres_fixture]
