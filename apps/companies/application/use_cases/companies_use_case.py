"""
Use case for companies.
"""

from __future__ import annotations

from apps.companies.application.services.companies_service import CompanyService
from apps.companies.application.services.dtos import CompanyServiceDTO
from apps.companies.application.use_cases.dtos import CompanyUseCaseDTO


class CompanyUseCase:
    """Use case for company operations."""

    def __init__(self, service: CompanyService) -> None:
        self._service = service

    def _to_dto(self, svc_dto: CompanyServiceDTO) -> CompanyUseCaseDTO:
        return CompanyUseCaseDTO(
            id=svc_dto.id,
            name=svc_dto.name,
            country=svc_dto.country,
            founded=svc_dto.founded,
            website=svc_dto.website,
        )

    def _to_service_dto(self, dto: CompanyUseCaseDTO) -> CompanyServiceDTO:
        return CompanyServiceDTO(
            id=dto.id,
            name=dto.name,
            country=dto.country,
            founded=dto.founded,
            website=dto.website,
        )

    def list_all(self) -> list[CompanyUseCaseDTO]:
        return [self._to_dto(d) for d in self._service.list_all()]

    def get_by_id(self, id: int) -> CompanyUseCaseDTO | None:
        result = self._service.get_by_id(id)
        return self._to_dto(result) if result else None

    def create(self, dto: CompanyUseCaseDTO) -> CompanyUseCaseDTO:
        return self._to_dto(self._service.create(self._to_service_dto(dto)))

    def update(self, dto: CompanyUseCaseDTO) -> CompanyUseCaseDTO:
        return self._to_dto(self._service.update(self._to_service_dto(dto)))

    def delete(self, id: int) -> None:
        self._service.delete(id)
