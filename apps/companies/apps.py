"""
AppConfig for companies.
"""

from __future__ import annotations

from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.companies"
    label = "companies"

    def import_models(self) -> None:
        import apps.companies.infrastructure.models  # noqa: F401

        super().import_models()
