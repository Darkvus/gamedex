"""
Repository interfaces for franchises domain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from apps.franchises.domain.entities import FranchiseEntity


class AbstractFranchiseRepository(ABC):
    """Abstract repository for franchises."""

    @abstractmethod
    def list_all(self) -> list[FranchiseEntity]: ...

    @abstractmethod
    def get_by_id(self, id: str) -> FranchiseEntity | None: ...

    @abstractmethod
    def create(self, entity: FranchiseEntity) -> FranchiseEntity: ...

    @abstractmethod
    def update(self, entity: FranchiseEntity) -> FranchiseEntity: ...

    @abstractmethod
    def delete(self, id: str) -> None: ...
