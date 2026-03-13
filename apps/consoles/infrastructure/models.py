"""
    Django ORM models for consoles.
"""
from __future__ import annotations

from pyms_django.models import BaseModel


class Consoles(BaseModel):
    """Consoles model.

    Add your fields here.
    """

    class Meta:
        app_label = "consoles"
        db_table = "consoles"
        verbose_name = "consoles"
        verbose_name_plural = "consoles"

    def __str__(self) -> str:
        return f"Consoles({self.pk})"
