"""
Entities for releases domain.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class ReleaseEntity:
    """Release domain entity."""

    id: str | None
    game_id: str
    region_id: str
    console_id: str | None
    release_date: date | None
