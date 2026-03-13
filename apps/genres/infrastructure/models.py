"""
    Django ORM models for genres.
"""
from __future__ import annotations

from pyms_django.models import BaseModel


class Genres(BaseModel):
    """Genres model.

    Add your fields here.
    """

    class Meta:
        app_label = "genres"
        db_table = "genres"
        verbose_name = "genres"
        verbose_name_plural = "genres"

    def __str__(self) -> str:
        return f"Genres({self.pk})"
