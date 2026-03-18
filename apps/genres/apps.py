"""
AppConfig for genres.
"""

from __future__ import annotations

from django.apps import AppConfig


class GenresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.genres"
    label = "genres"

    def import_models(self) -> None:
        import apps.genres.infrastructure.models  # noqa: F401

        super().import_models()
