"""
    DTOs for games use cases.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GameUseCaseDTO:
    """DTO used by the game use case layer."""

    id: int | None
    name: str
    slug: str
    description: str
    release_year: int | None
    genre_id: int | None
    developer_id: int | None
    publisher_id: int | None
