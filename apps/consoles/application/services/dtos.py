"""
    DTOs for consoles application services.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConsoleServiceDTO:
    """DTO used by the console service layer."""

    id: int | None
    name: str
    manufacturer: str
    release_year: int | None
    generation: int | None
    type: str
