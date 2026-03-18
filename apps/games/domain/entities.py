"""
Entities for games domain.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GameEntity:
    """Game domain entity."""

    id: int | None
    name: str
    slug: str
    description: str
    release_year: int | None
    genre_id: int | None
    developer_id: int | None
    publisher_id: int | None
