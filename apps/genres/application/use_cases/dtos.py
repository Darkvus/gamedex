"""
    DTOs for genres use cases.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GenreUseCaseDTO:
    """DTO used by the genre use case layer."""

    id: int | None
    name: str
    description: str
