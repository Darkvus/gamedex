"""
    AppConfig for consoles.
"""
from __future__ import annotations

from django.apps import AppConfig


class ConsolesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.consoles"
    label = "consoles"
