"""
Use case for genres.
"""

from __future__ import annotations

from apps.genres.application.services.dtos import GenreServiceDTO
from apps.genres.application.services.genres_service import GenreService
from apps.genres.application.use_cases.dtos import GenreUseCaseDTO


class GenreUseCase:
    """Use case for genre operations."""

    def __init__(self, service: GenreService) -> None:
        self._service = service

    def _to_dto(self, svc_dto: GenreServiceDTO) -> GenreUseCaseDTO:
        return GenreUseCaseDTO(id=svc_dto.id, name=svc_dto.name, description=svc_dto.description)

    def _to_service_dto(self, dto: GenreUseCaseDTO) -> GenreServiceDTO:
        return GenreServiceDTO(id=dto.id, name=dto.name, description=dto.description)

    def list_all(self) -> list[GenreUseCaseDTO]:
        return [self._to_dto(d) for d in self._service.list_all()]

    def get_by_id(self, id: int) -> GenreUseCaseDTO | None:
        result = self._service.get_by_id(id)
        return self._to_dto(result) if result else None

    def create(self, dto: GenreUseCaseDTO) -> GenreUseCaseDTO:
        return self._to_dto(self._service.create(self._to_service_dto(dto)))

    def update(self, dto: GenreUseCaseDTO) -> GenreUseCaseDTO:
        return self._to_dto(self._service.update(self._to_service_dto(dto)))

    def delete(self, id: int) -> None:
        self._service.delete(id)
