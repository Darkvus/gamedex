"""
Use case for games.
"""

from __future__ import annotations

from apps.games.application.services.dtos import GameServiceDTO
from apps.games.application.services.games_service import GameService
from apps.games.application.use_cases.dtos import GameUseCaseDTO


class GameUseCase:
    """Use case for game operations."""

    def __init__(self, service: GameService) -> None:
        self._service = service

    def _to_dto(self, svc_dto: GameServiceDTO) -> GameUseCaseDTO:
        return GameUseCaseDTO(
            id=svc_dto.id,
            name=svc_dto.name,
            slug=svc_dto.slug,
            description=svc_dto.description,
            release_year=svc_dto.release_year,
            genre_id=svc_dto.genre_id,
            developer_id=svc_dto.developer_id,
            publisher_id=svc_dto.publisher_id,
        )

    def _to_service_dto(self, dto: GameUseCaseDTO) -> GameServiceDTO:
        return GameServiceDTO(
            id=dto.id,
            name=dto.name,
            slug=dto.slug,
            description=dto.description,
            release_year=dto.release_year,
            genre_id=dto.genre_id,
            developer_id=dto.developer_id,
            publisher_id=dto.publisher_id,
        )

    def list_all(self) -> list[GameUseCaseDTO]:
        return [self._to_dto(d) for d in self._service.list_all()]

    def get_by_id(self, id: int) -> GameUseCaseDTO | None:
        result = self._service.get_by_id(id)
        return self._to_dto(result) if result else None

    def create(self, dto: GameUseCaseDTO) -> GameUseCaseDTO:
        return self._to_dto(self._service.create(self._to_service_dto(dto)))

    def update(self, dto: GameUseCaseDTO) -> GameUseCaseDTO:
        return self._to_dto(self._service.update(self._to_service_dto(dto)))

    def delete(self, id: int) -> None:
        self._service.delete(id)
