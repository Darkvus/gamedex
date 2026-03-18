"""
DTOs for consoles use cases.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConsoleUseCaseDTO:
    """DTO used by the console use case layer."""

    id: int | None
    name: str
    manufacturer: str
    release_year: int | None
    generation: int | None
    type: str
