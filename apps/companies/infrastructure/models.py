"""
    Django ORM models for companies.
"""
from __future__ import annotations

from pyms_django.models import BaseModel


class Companies(BaseModel):
    """Companies model.

    Add your fields here.
    """

    class Meta:
        app_label = "companies"
        db_table = "companies"
        verbose_name = "companies"
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return f"Companies({self.pk})"
