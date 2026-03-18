"""
Use case for consoles.
"""

from __future__ import annotations

from apps.consoles.application.services.consoles_service import ConsoleService
from apps.consoles.application.services.dtos import ConsoleServiceDTO
from apps.consoles.application.use_cases.dtos import ConsoleUseCaseDTO


class ConsoleUseCase:
    """Use case for console operations."""

    def __init__(self, service: ConsoleService) -> None:
        self._service = service

    def _to_dto(self, svc_dto: ConsoleServiceDTO) -> ConsoleUseCaseDTO:
        return ConsoleUseCaseDTO(
            id=svc_dto.id,
            name=svc_dto.name,
            manufacturer=svc_dto.manufacturer,
            release_year=svc_dto.release_year,
            generation=svc_dto.generation,
            type=svc_dto.type,
        )

    def _to_service_dto(self, dto: ConsoleUseCaseDTO) -> ConsoleServiceDTO:
        return ConsoleServiceDTO(
            id=dto.id,
            name=dto.name,
            manufacturer=dto.manufacturer,
            release_year=dto.release_year,
            generation=dto.generation,
            type=dto.type,
        )

    def list_all(self) -> list[ConsoleUseCaseDTO]:
        return [self._to_dto(d) for d in self._service.list_all()]

    def get_by_id(self, id: int) -> ConsoleUseCaseDTO | None:
        result = self._service.get_by_id(id)
        return self._to_dto(result) if result else None

    def create(self, dto: ConsoleUseCaseDTO) -> ConsoleUseCaseDTO:
        return self._to_dto(self._service.create(self._to_service_dto(dto)))

    def update(self, dto: ConsoleUseCaseDTO) -> ConsoleUseCaseDTO:
        return self._to_dto(self._service.update(self._to_service_dto(dto)))

    def delete(self, id: int) -> None:
        self._service.delete(id)
