"""
    Django ORM models for franchises.
"""
from __future__ import annotations

from pyms_django.models import BaseModel


class Franchises(BaseModel):
    """Franchises model.

    Add your fields here.
    """

    class Meta:
        app_label = "franchises"
        db_table = "franchises"
        verbose_name = "franchises"
        verbose_name_plural = "franchises"

    def __str__(self) -> str:
        return f"Franchises({self.pk})"
