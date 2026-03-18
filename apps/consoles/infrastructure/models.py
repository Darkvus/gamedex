"""
Django ORM models for consoles.
"""

from __future__ import annotations

from django.db import models
from pyms_django.models import BaseModel

CONSOLE_TYPE_CHOICES = [
    ("home", "Home"),
    ("handheld", "Handheld"),
    ("hybrid", "Hybrid"),
    ("arcade", "Arcade"),
    ("other", "Other"),
]


class Consoles(BaseModel):
    """Consoles model."""

    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200, blank=True, default="")
    release_year = models.PositiveSmallIntegerField(null=True, blank=True)
    generation = models.PositiveSmallIntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=CONSOLE_TYPE_CHOICES, default="home")

    class Meta:
        app_label = "consoles"
        db_table = "consoles"
        ordering = ["name"]
        verbose_name = "console"

    def __str__(self) -> str:
        return self.name
