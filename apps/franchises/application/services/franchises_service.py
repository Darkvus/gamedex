"""
Service for franchises.
"""

from __future__ import annotations

from apps.franchises.application.services.dtos import FranchiseServiceDTO
from apps.franchises.domain.entities import FranchiseEntity
from apps.franchises.domain.repositories import AbstractFranchiseRepository


class FranchiseService:
    """Application service for franchises."""

    def __init__(self, repository: AbstractFranchiseRepository) -> None:
        self._repository = repository

    def _to_dto(self, entity: FranchiseEntity) -> FranchiseServiceDTO:
        return FranchiseServiceDTO(
            id=entity.id,
            name=entity.name,
            slug=entity.slug,
            description=entity.description,
            founded_year=entity.founded_year,
        )

    def _to_entity(self, dto: FranchiseServiceDTO) -> FranchiseEntity:
        return FranchiseEntity(
            id=dto.id,
            name=dto.name,
            slug=dto.slug,
            description=dto.description,
            founded_year=dto.founded_year,
        )

    def list_all(self) -> list[FranchiseServiceDTO]:
        return [self._to_dto(e) for e in self._repository.list_all()]

    def get_by_id(self, id: str) -> FranchiseServiceDTO | None:
        entity = self._repository.get_by_id(id)
        return self._to_dto(entity) if entity else None

    def create(self, dto: FranchiseServiceDTO) -> FranchiseServiceDTO:
        return self._to_dto(self._repository.create(self._to_entity(dto)))

    def update(self, dto: FranchiseServiceDTO) -> FranchiseServiceDTO:
        return self._to_dto(self._repository.update(self._to_entity(dto)))

    def delete(self, id: str) -> None:
        self._repository.delete(id)
