"""
Repository interfaces for companies domain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from apps.companies.domain.entities import CompanyEntity


class AbstractCompanyRepository(ABC):
    """Abstract repository for companies."""

    @abstractmethod
    def list_all(self) -> list[CompanyEntity]: ...

    @abstractmethod
    def get_by_id(self, id: int) -> CompanyEntity | None: ...

    @abstractmethod
    def create(self, entity: CompanyEntity) -> CompanyEntity: ...

    @abstractmethod
    def update(self, entity: CompanyEntity) -> CompanyEntity: ...

    @abstractmethod
    def delete(self, id: int) -> None: ...
