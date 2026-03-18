"""
    Use case for franchises.
"""
from __future__ import annotations

from apps.franchises.application.services.dtos import FranchiseServiceDTO
from apps.franchises.application.services.franchises_service import FranchiseService
from apps.franchises.application.use_cases.dtos import FranchiseUseCaseDTO


class FranchiseUseCase:
    """Use case for franchise operations."""

    def __init__(self, service: FranchiseService) -> None:
        self._service = service

    def _to_dto(self, svc_dto: FranchiseServiceDTO) -> FranchiseUseCaseDTO:
        return FranchiseUseCaseDTO(
            id=svc_dto.id,
            name=svc_dto.name,
            slug=svc_dto.slug,
            description=svc_dto.description,
            founded_year=svc_dto.founded_year,
        )

    def _to_service_dto(self, dto: FranchiseUseCaseDTO) -> FranchiseServiceDTO:
        return FranchiseServiceDTO(
            id=dto.id,
            name=dto.name,
            slug=dto.slug,
            description=dto.description,
            founded_year=dto.founded_year,
        )

    def list_all(self) -> list[FranchiseUseCaseDTO]:
        return [self._to_dto(d) for d in self._service.list_all()]

    def get_by_id(self, id: str) -> FranchiseUseCaseDTO | None:
        result = self._service.get_by_id(id)
        return self._to_dto(result) if result else None

    def create(self, dto: FranchiseUseCaseDTO) -> FranchiseUseCaseDTO:
        return self._to_dto(self._service.create(self._to_service_dto(dto)))

    def update(self, dto: FranchiseUseCaseDTO) -> FranchiseUseCaseDTO:
        return self._to_dto(self._service.update(self._to_service_dto(dto)))

    def delete(self, id: str) -> None:
        self._service.delete(id)
