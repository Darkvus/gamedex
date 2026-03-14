from __future__ import annotations

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.companies.infrastructure.models import Companies


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Companies
        fields = ("id", "name", "country", "founded", "website", "active")
        import_id_fields = ("id",)


@admin.register(Companies)
class CompanyAdmin(ImportExportModelAdmin):
    resource_classes = [CompanyResource]
    list_display = ("name", "country", "founded", "active")
    search_fields = ("name", "country")
