"""
Entities for genres domain.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GenreEntity:
    """Genre domain entity."""

    id: int | None
    name: str
    description: str
