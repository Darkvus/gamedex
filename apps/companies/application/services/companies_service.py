"""
Service for companies.
"""

from __future__ import annotations

from apps.companies.application.services.dtos import CompanyServiceDTO
from apps.companies.domain.entities import CompanyEntity
from apps.companies.domain.repositories import AbstractCompanyRepository


class CompanyService:
    """Application service for companies."""

    def __init__(self, repository: AbstractCompanyRepository) -> None:
        self._repository = repository

    def _to_dto(self, entity: CompanyEntity) -> CompanyServiceDTO:
        return CompanyServiceDTO(
            id=entity.id,
            name=entity.name,
            country=entity.country,
            founded=entity.founded,
            website=entity.website,
        )

    def _to_entity(self, dto: CompanyServiceDTO) -> CompanyEntity:
        return CompanyEntity(
            id=dto.id,
            name=dto.name,
            country=dto.country,
            founded=dto.founded,
            website=dto.website,
        )

    def list_all(self) -> list[CompanyServiceDTO]:
        return [self._to_dto(e) for e in self._repository.list_all()]

    def get_by_id(self, id: int) -> CompanyServiceDTO | None:
        entity = self._repository.get_by_id(id)
        return self._to_dto(entity) if entity else None

    def create(self, dto: CompanyServiceDTO) -> CompanyServiceDTO:
        return self._to_dto(self._repository.create(self._to_entity(dto)))

    def update(self, dto: CompanyServiceDTO) -> CompanyServiceDTO:
        return self._to_dto(self._repository.update(self._to_entity(dto)))

    def delete(self, id: int) -> None:
        self._repository.delete(id)
