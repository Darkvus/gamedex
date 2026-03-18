"""
Repository implementation for releases.
"""

from __future__ import annotations

from apps.releases.domain.entities import ReleaseEntity
from apps.releases.domain.repositories import AbstractReleaseRepository
from apps.releases.infrastructure.models import Releases


class ReleaseRepository(AbstractReleaseRepository):
    """Django ORM implementation of ReleaseRepository."""

    def _to_entity(self, obj: Releases) -> ReleaseEntity:
        return ReleaseEntity(
            id=str(obj.id),
            game_id=str(obj.game_id),
            region_id=str(obj.region_id),
            console_id=str(obj.console_id) if obj.console_id else None,
            release_date=obj.release_date,
        )

    def list_all(self) -> list[ReleaseEntity]:
        return [self._to_entity(obj) for obj in Releases.objects.select_related("game", "region", "console").all()]

    def get_by_id(self, id: str) -> ReleaseEntity | None:
        try:
            return self._to_entity(Releases.objects.get(pk=id))
        except Releases.DoesNotExist:
            return None
