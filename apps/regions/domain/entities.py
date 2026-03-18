"""
    Entities for regions domain.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RegionEntity:
    """Region domain entity."""

    id: str | None
    code: str
    name: str
