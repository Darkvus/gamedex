"""
    Entities for franchises domain.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FranchiseEntity:
    """Franchise domain entity."""

    id: str | None
    name: str
    slug: str
    description: str
    founded_year: int | None
