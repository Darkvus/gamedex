from __future__ import annotations

import os

import tablib
from django.contrib import admin, messages
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from modeltranslation.admin import TranslationAdmin

from apps.companies.infrastructure.models import Companies
from apps.consoles.infrastructure.models import Consoles
from apps.games.infrastructure.models import Games
from apps.genres.infrastructure.models import Genres

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "import", "games.json")


class GameResource(resources.ModelResource):
    genre = fields.Field(
        column_name="genre",
        attribute="genre",
        widget=ForeignKeyWidget(Genres, field="name_en"),
    )
    developer = fields.Field(
        column_name="developer",
        attribute="developer",
        widget=ForeignKeyWidget(Companies, field="name_en"),
    )
    publisher = fields.Field(
        column_name="publisher",
        attribute="publisher",
        widget=ForeignKeyWidget(Companies, field="name_en"),
    )
    consoles = fields.Field(
        column_name="consoles",
        attribute="consoles",
        widget=ManyToManyWidget(Consoles, field="name_en", separator=","),
    )

    class Meta:
        model = Games
        fields = (
            "id",
            "name",
            "name_en",
            "name_es",
            "slug",
            "description",
            "description_en",
            "description_es",
            "release_year",
            "genre",
            "developer",
            "publisher",
            "consoles",
            "active",
        )
        import_id_fields = ("name_en",)


def load_games_fixture(modeladmin, request, queryset):
    with open(FIXTURE_PATH) as f:
        dataset = tablib.Dataset().load(f.read())
    result = GameResource().import_data(dataset, dry_run=False, raise_errors=True)
    messages.success(request, f"Games fixture loaded: {result.totals}")


load_games_fixture.short_description = "Load games from fixture"


@admin.register(Games)
class GameAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_classes = [GameResource]
    list_display = ("name", "release_year", "genre", "developer", "publisher", "active")
    search_fields = ("name", "slug")
    list_filter = ("genre", "developer", "release_year")
    filter_horizontal = ("consoles",)
    actions = [load_games_fixture]
