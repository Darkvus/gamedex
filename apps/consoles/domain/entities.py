"""
    Entities for consoles domain.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConsoleEntity:
    """Console domain entity."""

    id: int | None
    name: str
    manufacturer: str
    release_year: int | None
    generation: int | None
    type: str
