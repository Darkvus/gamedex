"""
    DTOs for franchises use cases.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FranchiseUseCaseDTO:
    """DTO used by the franchise use case layer."""

    id: str | None
    name: str
    slug: str
    description: str
    founded_year: int | None
