"""
Repository implementation for franchises.
"""

from __future__ import annotations

from apps.franchises.domain.entities import FranchiseEntity
from apps.franchises.domain.repositories import AbstractFranchiseRepository
from apps.franchises.infrastructure.models import Franchises


class FranchiseRepository(AbstractFranchiseRepository):
    """Django ORM implementation of FranchiseRepository."""

    def _to_entity(self, obj: Franchises) -> FranchiseEntity:
        return FranchiseEntity(
            id=str(obj.id),
            name=obj.name,
            slug=obj.slug,
            description=obj.description,
            founded_year=obj.founded_year,
        )

    def list_all(self) -> list[FranchiseEntity]:
        return [self._to_entity(obj) for obj in Franchises.objects.all()]

    def get_by_id(self, id: str) -> FranchiseEntity | None:
        try:
            return self._to_entity(Franchises.objects.get(pk=id))
        except Franchises.DoesNotExist:
            return None

    def create(self, entity: FranchiseEntity) -> FranchiseEntity:
        obj = Franchises.objects.create(
            name=entity.name,
            description=entity.description,
            founded_year=entity.founded_year,
        )
        return self._to_entity(obj)

    def update(self, entity: FranchiseEntity) -> FranchiseEntity:
        Franchises.objects.filter(pk=entity.id).update(
            name=entity.name,
            description=entity.description,
            founded_year=entity.founded_year,
        )
        return self._to_entity(Franchises.objects.get(pk=entity.id))

    def delete(self, id: str) -> None:
        Franchises.objects.filter(pk=id).delete()
