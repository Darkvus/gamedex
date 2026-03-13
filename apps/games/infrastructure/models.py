"""
    Django ORM models for games.
"""
from __future__ import annotations

from pyms_django.models import BaseModel


class Games(BaseModel):
    """Games model.

    Add your fields here.
    """

    class Meta:
        app_label = "games"
        db_table = "games"
        verbose_name = "games"
        verbose_name_plural = "games"

    def __str__(self) -> str:
        return f"Games({self.pk})"
