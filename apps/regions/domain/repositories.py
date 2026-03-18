"""
Repository interfaces for regions domain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from apps.regions.domain.entities import RegionEntity


class AbstractRegionRepository(ABC):
    """Abstract repository for regions."""

    @abstractmethod
    def list_all(self) -> list[RegionEntity]: ...

    @abstractmethod
    def get_by_id(self, id: str) -> RegionEntity | None: ...
