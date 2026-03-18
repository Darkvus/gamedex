"""
    Django ORM models for franchises.
"""
from __future__ import annotations

from django.db import models
from django.utils.text import slugify
from pyms_django.models import BaseModel


class Franchises(BaseModel):
    """Franchises model — a series of related games (e.g. Mario, Zelda)."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True, default="")
    founded_year = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        app_label = "franchises"
        db_table = "franchises"
        ordering = ["name"]
        verbose_name = "franchise"
        verbose_name_plural = "franchises"

    def save(self, *args: object, **kwargs: object) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
