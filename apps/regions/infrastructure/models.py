from __future__ import annotations

from django.db import models
from pyms_django.models import BaseModel


class Regions(BaseModel):
    """Regions model."""

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "regions"
        db_table = "regions"
        ordering = ["code"]
        verbose_name = "region"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"
