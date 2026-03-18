"""
AppConfig for games.
"""

from __future__ import annotations

from django.apps import AppConfig


class GamesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.games"
    label = "games"

    def import_models(self) -> None:
        import apps.games.infrastructure.models  # noqa: F401

        super().import_models()
