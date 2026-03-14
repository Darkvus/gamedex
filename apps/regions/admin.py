from __future__ import annotations
import os
import tablib
from django.contrib import admin, messages
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin
from apps.regions.infrastructure.models import Regions

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "import", "regions.json")

class RegionResource(resources.ModelResource):
    class Meta:
        model = Regions
        fields = ("id", "code", "name", "name_en", "name_es", "active")
        import_id_fields = ("code",)

def load_regions_fixture(modeladmin, request, queryset):
    with open(FIXTURE_PATH) as f:
        dataset = tablib.Dataset().load(f.read())
    result = RegionResource().import_data(dataset, dry_run=False, raise_errors=True)
    messages.success(request, f"Regions fixture loaded: {result.totals}")

load_regions_fixture.short_description = "Load regions from fixture"

@admin.register(Regions)
class RegionAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_classes = [RegionResource]
    list_display = ("code", "name", "active")
    search_fields = ("code", "name")
    actions = [load_regions_fixture]
