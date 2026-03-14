"""
    Entities for companies domain.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CompanyEntity:
    """Company domain entity."""

    id: int | None
    name: str
    country: str
    founded: int | None
    website: str
