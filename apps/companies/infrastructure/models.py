"""
Django ORM models for companies.
"""

from __future__ import annotations

from django.db import models
from pyms_django.models import BaseModel


class Companies(BaseModel):
    """Companies model."""

    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=100, blank=True, default="")
    founded = models.PositiveSmallIntegerField(null=True, blank=True)
    website = models.URLField(blank=True, default="")

    class Meta:
        app_label = "companies"
        db_table = "companies"
        ordering = ["name"]
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return self.name
