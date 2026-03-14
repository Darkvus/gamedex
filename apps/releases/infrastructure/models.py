from __future__ import annotations
from django.db import models
from pyms_django.models import BaseModel

class Releases(BaseModel):
    """Release model — tracks a game's release in a specific region."""
    game = models.ForeignKey(
        "games.Games",
        on_delete=models.CASCADE,
        related_name="releases",
    )
    region = models.ForeignKey(
        "regions.Regions",
        on_delete=models.CASCADE,
        related_name="releases",
    )
    console = models.ForeignKey(
        "consoles.Consoles",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="releases",
    )
    release_date = models.DateField(null=True, blank=True)

    class Meta:
        app_label = "releases"
        db_table = "releases"
        ordering = ["release_date"]
        verbose_name = "release"
        unique_together = [("game", "region", "console")]

    def __str__(self) -> str:
        return f"{self.game} — {self.region} ({self.release_date or 'TBD'})"
