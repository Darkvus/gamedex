"""
Django ORM repository implementation for companies.
"""

from __future__ import annotations

from apps.companies.domain.entities import CompanyEntity
from apps.companies.domain.repositories import AbstractCompanyRepository
from apps.companies.infrastructure.models import Companies


class DjangoCompanyRepository(AbstractCompanyRepository):
    """Django ORM implementation of the company repository."""

    def _to_entity(self, obj: Companies) -> CompanyEntity:
        return CompanyEntity(
            id=obj.pk,
            name=obj.name,
            country=obj.country,
            founded=obj.founded,
            website=obj.website,
        )

    def list_all(self) -> list[CompanyEntity]:
        return [self._to_entity(obj) for obj in Companies.objects.all()]

    def get_by_id(self, id: int) -> CompanyEntity | None:
        try:
            return self._to_entity(Companies.objects.get(pk=id))
        except Companies.DoesNotExist:
            return None

    def create(self, entity: CompanyEntity) -> CompanyEntity:
        obj = Companies.objects.create(
            name=entity.name,
            country=entity.country,
            founded=entity.founded,
            website=entity.website,
        )
        return self._to_entity(obj)

    def update(self, entity: CompanyEntity) -> CompanyEntity:
        Companies.objects.filter(pk=entity.id).update(
            name=entity.name,
            country=entity.country,
            founded=entity.founded,
            website=entity.website,
        )
        return self._to_entity(Companies.objects.get(pk=entity.id))

    def delete(self, id: int) -> None:
        Companies.objects.filter(pk=id).delete()
