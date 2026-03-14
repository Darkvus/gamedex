"""
    DTOs for genres application services.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GenreServiceDTO:
    """DTO used by the genre service layer."""

    id: int | None
    name: str
    description: str
