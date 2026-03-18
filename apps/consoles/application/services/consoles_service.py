"""
Service for consoles.
"""

from __future__ import annotations

from apps.consoles.application.services.dtos import ConsoleServiceDTO
from apps.consoles.domain.entities import ConsoleEntity
from apps.consoles.domain.repositories import AbstractConsoleRepository


class ConsoleService:
    """Application service for consoles."""

    def __init__(self, repository: AbstractConsoleRepository) -> None:
        self._repository = repository

    def _to_dto(self, entity: ConsoleEntity) -> ConsoleServiceDTO:
        return ConsoleServiceDTO(
            id=entity.id,
            name=entity.name,
            manufacturer=entity.manufacturer,
            release_year=entity.release_year,
            generation=entity.generation,
            type=entity.type,
        )

    def _to_entity(self, dto: ConsoleServiceDTO) -> ConsoleEntity:
        return ConsoleEntity(
            id=dto.id,
            name=dto.name,
            manufacturer=dto.manufacturer,
            release_year=dto.release_year,
            generation=dto.generation,
            type=dto.type,
        )

    def list_all(self) -> list[ConsoleServiceDTO]:
        return [self._to_dto(e) for e in self._repository.list_all()]

    def get_by_id(self, id: int) -> ConsoleServiceDTO | None:
        entity = self._repository.get_by_id(id)
        return self._to_dto(entity) if entity else None

    def create(self, dto: ConsoleServiceDTO) -> ConsoleServiceDTO:
        return self._to_dto(self._repository.create(self._to_entity(dto)))

    def update(self, dto: ConsoleServiceDTO) -> ConsoleServiceDTO:
        return self._to_dto(self._repository.update(self._to_entity(dto)))

    def delete(self, id: int) -> None:
        self._repository.delete(id)
