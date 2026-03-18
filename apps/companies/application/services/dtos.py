"""
DTOs for companies application services.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CompanyServiceDTO:
    """DTO used by the company service layer."""

    id: int | None
    name: str
    country: str
    founded: int | None
    website: str
