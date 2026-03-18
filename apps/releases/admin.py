from __future__ import annotations

import os

import tablib
from django.contrib import admin, messages
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from apps.consoles.infrastructure.models import Consoles
from apps.games.infrastructure.models import Games
from apps.regions.infrastructure.models import Regions
from apps.releases.infrastructure.models import Releases

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "import", "releases.json")


class ReleaseResource(resources.ModelResource):
    game = fields.Field(column_name="game", attribute="game", widget=ForeignKeyWidget(Games, field="name_en"))
    region = fields.Field(column_name="region", attribute="region", widget=ForeignKeyWidget(Regions, field="code"))
    console = fields.Field(
        column_name="console", attribute="console", widget=ForeignKeyWidget(Consoles, field="name_en")
    )

    class Meta:
        model = Releases
        fields = ("id", "game", "region", "console", "release_date", "active")
        import_id_fields = ("game", "region", "console")


def load_releases_fixture(modeladmin, request, queryset):
    with open(FIXTURE_PATH) as f:
        dataset = tablib.Dataset().load(f.read())
    result = ReleaseResource().import_data(dataset, dry_run=False, raise_errors=True)
    messages.success(request, f"Releases fixture loaded: {result.totals}")


load_releases_fixture.short_description = "Load releases from fixture"


@admin.register(Releases)
class ReleaseAdmin(ImportExportModelAdmin):
    resource_classes = [ReleaseResource]
    list_display = ("game", "region", "console", "release_date", "active")
    list_filter = ("region", "console")
    search_fields = ("game__name",)
    actions = [load_releases_fixture]
