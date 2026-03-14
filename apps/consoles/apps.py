"""
    AppConfig for consoles.
"""
from __future__ import annotations

from django.apps import AppConfig


class ConsolesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.consoles"
    label = "consoles"

    def import_models(self) -> None:
        import apps.consoles.infrastructure.models  # noqa: F401
        super().import_models()
