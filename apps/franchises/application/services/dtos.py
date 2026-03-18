"""
    DTOs for franchises application services.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FranchiseServiceDTO:
    """DTO used by the franchise service layer."""

    id: str | None
    name: str
    slug: str
    description: str
    founded_year: int | None
