from __future__ import annotations

import os

import tablib
from django.contrib import admin, messages
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin

from apps.companies.infrastructure.models import Companies

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "import", "companies.json")


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Companies
        fields = ("id", "name", "name_en", "name_es", "country", "founded", "website", "active")
        import_id_fields = ("name_en",)


def load_companies_fixture(modeladmin, request, queryset):
    with open(FIXTURE_PATH) as f:
        dataset = tablib.Dataset().load(f.read())
    result = CompanyResource().import_data(dataset, dry_run=False, raise_errors=True)
    messages.success(request, f"Companies fixture loaded: {result.totals}")


load_companies_fixture.short_description = "Load companies from fixture"


@admin.register(Companies)
class CompanyAdmin(ImportExportModelAdmin, TranslationAdmin):
    resource_classes = [CompanyResource]
    list_display = ("name", "country", "founded", "active")
    search_fields = ("name", "country")
    actions = [load_companies_fixture]
