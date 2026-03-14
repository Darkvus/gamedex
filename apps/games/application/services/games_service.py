"""
    Service for games.
"""
from __future__ import annotations

from apps.games.application.services.dtos import GameServiceDTO
from apps.games.domain.entities import GameEntity
from apps.games.domain.repositories import AbstractGameRepository


class GameService:
    """Application service for games."""

    def __init__(self, repository: AbstractGameRepository) -> None:
        self._repository = repository

    def _to_dto(self, entity: GameEntity) -> GameServiceDTO:
        return GameServiceDTO(
            id=entity.id,
            name=entity.name,
            slug=entity.slug,
            description=entity.description,
            release_year=entity.release_year,
            genre_id=entity.genre_id,
            developer_id=entity.developer_id,
            publisher_id=entity.publisher_id,
        )

    def _to_entity(self, dto: GameServiceDTO) -> GameEntity:
        return GameEntity(
            id=dto.id,
            name=dto.name,
            slug=dto.slug,
            description=dto.description,
            release_year=dto.release_year,
            genre_id=dto.genre_id,
            developer_id=dto.developer_id,
            publisher_id=dto.publisher_id,
        )

    def list_all(self) -> list[GameServiceDTO]:
        return [self._to_dto(e) for e in self._repository.list_all()]

    def get_by_id(self, id: int) -> GameServiceDTO | None:
        entity = self._repository.get_by_id(id)
        return self._to_dto(entity) if entity else None

    def create(self, dto: GameServiceDTO) -> GameServiceDTO:
        return self._to_dto(self._repository.create(self._to_entity(dto)))

    def update(self, dto: GameServiceDTO) -> GameServiceDTO:
        return self._to_dto(self._repository.update(self._to_entity(dto)))

    def delete(self, id: int) -> None:
        self._repository.delete(id)
