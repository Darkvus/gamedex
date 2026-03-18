"""
Django ORM models for games.
"""

from __future__ import annotations

from django.db import models
from django.utils.text import slugify
from pyms_django.models import BaseModel


class Games(BaseModel):
    """Games model."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True, default="")
    release_year = models.PositiveSmallIntegerField(null=True, blank=True)
    genre = models.ForeignKey(
        "genres.Genres",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="games",
    )
    developer = models.ForeignKey(
        "companies.Companies",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="developed_games",
    )
    publisher = models.ForeignKey(
        "companies.Companies",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="published_games",
    )
    cover_url = models.URLField(max_length=500, blank=True, default="")
    franchise = models.ForeignKey(
        "franchises.Franchises",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="games",
    )
    consoles = models.ManyToManyField(
        "consoles.Consoles",
        blank=True,
        related_name="games",
    )

    class Meta:
        app_label = "games"
        db_table = "games"
        ordering = ["name"]
        verbose_name = "game"

    def save(self, *args: object, **kwargs: object) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
