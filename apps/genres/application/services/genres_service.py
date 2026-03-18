"""
Service for genres.
"""

from __future__ import annotations

from apps.genres.application.services.dtos import GenreServiceDTO
from apps.genres.domain.entities import GenreEntity
from apps.genres.domain.repositories import AbstractGenreRepository


class GenreService:
    """Application service for genres."""

    def __init__(self, repository: AbstractGenreRepository) -> None:
        self._repository = repository

    def _to_dto(self, entity: GenreEntity) -> GenreServiceDTO:
        return GenreServiceDTO(id=entity.id, name=entity.name, description=entity.description)

    def _to_entity(self, dto: GenreServiceDTO) -> GenreEntity:
        return GenreEntity(id=dto.id, name=dto.name, description=dto.description)

    def list_all(self) -> list[GenreServiceDTO]:
        return [self._to_dto(e) for e in self._repository.list_all()]

    def get_by_id(self, id: int) -> GenreServiceDTO | None:
        entity = self._repository.get_by_id(id)
        return self._to_dto(entity) if entity else None

    def create(self, dto: GenreServiceDTO) -> GenreServiceDTO:
        return self._to_dto(self._repository.create(self._to_entity(dto)))

    def update(self, dto: GenreServiceDTO) -> GenreServiceDTO:
        return self._to_dto(self._repository.update(self._to_entity(dto)))

    def delete(self, id: int) -> None:
        self._repository.delete(id)
