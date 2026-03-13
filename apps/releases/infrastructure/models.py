"""
    Django ORM models for releases.
"""
from __future__ import annotations

from pyms_django.models import BaseModel


class Releases(BaseModel):
    """Releases model.

    Add your fields here.
    """

    class Meta:
        app_label = "releases"
        db_table = "releases"
        verbose_name = "releases"
        verbose_name_plural = "releases"

    def __str__(self) -> str:
        return f"Releases({self.pk})"
