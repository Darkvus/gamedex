"""
    Repository implementation for regions.
"""
from __future__ import annotations

from apps.regions.domain.entities import RegionEntity
from apps.regions.domain.repositories import AbstractRegionRepository
from apps.regions.infrastructure.models import Regions


class RegionRepository(AbstractRegionRepository):
    """Django ORM implementation of RegionRepository."""

    def _to_entity(self, obj: Regions) -> RegionEntity:
        return RegionEntity(id=str(obj.id), code=obj.code, name=obj.name)

    def list_all(self) -> list[RegionEntity]:
        return [self._to_entity(obj) for obj in Regions.objects.all()]

    def get_by_id(self, id: str) -> RegionEntity | None:
        try:
            return self._to_entity(Regions.objects.get(pk=id))
        except Regions.DoesNotExist:
            return None
