"""
Repository interfaces for releases domain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from apps.releases.domain.entities import ReleaseEntity


class AbstractReleaseRepository(ABC):
    """Abstract repository for releases."""

    @abstractmethod
    def list_all(self) -> list[ReleaseEntity]: ...

    @abstractmethod
    def get_by_id(self, id: str) -> ReleaseEntity | None: ...
