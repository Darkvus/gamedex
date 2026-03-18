"""
DTOs for companies use cases.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CompanyUseCaseDTO:
    """DTO used by the company use case layer."""

    id: int | None
    name: str
    country: str
    founded: int | None
    website: str
