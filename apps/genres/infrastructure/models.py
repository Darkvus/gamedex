"""
Django ORM models for genres.
"""

from __future__ import annotations

from django.db import models
from pyms_django.models import BaseModel


class Genres(BaseModel):
    """Genres model."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")

    class Meta:
        app_label = "genres"
        db_table = "genres"
        ordering = ["name"]
        verbose_name = "genre"

    def __str__(self) -> str:
        return self.name
