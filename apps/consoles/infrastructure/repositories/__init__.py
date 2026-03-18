"""
Django ORM repository implementation for consoles.
"""

from __future__ import annotations

from apps.consoles.domain.entities import ConsoleEntity
from apps.consoles.domain.repositories import AbstractConsoleRepository
from apps.consoles.infrastructure.models import Consoles


class DjangoConsoleRepository(AbstractConsoleRepository):
    """Django ORM implementation of the console repository."""

    def _to_entity(self, obj: Consoles) -> ConsoleEntity:
        return ConsoleEntity(
            id=obj.pk,
            name=obj.name,
            manufacturer=obj.manufacturer,
            release_year=obj.release_year,
            generation=obj.generation,
            type=obj.type,
        )

    def list_all(self) -> list[ConsoleEntity]:
        return [self._to_entity(obj) for obj in Consoles.objects.all()]

    def get_by_id(self, id: int) -> ConsoleEntity | None:
        try:
            return self._to_entity(Consoles.objects.get(pk=id))
        except Consoles.DoesNotExist:
            return None

    def create(self, entity: ConsoleEntity) -> ConsoleEntity:
        obj = Consoles.objects.create(
            name=entity.name,
            manufacturer=entity.manufacturer,
            release_year=entity.release_year,
            generation=entity.generation,
            type=entity.type,
        )
        return self._to_entity(obj)

    def update(self, entity: ConsoleEntity) -> ConsoleEntity:
        Consoles.objects.filter(pk=entity.id).update(
            name=entity.name,
            manufacturer=entity.manufacturer,
            release_year=entity.release_year,
            generation=entity.generation,
            type=entity.type,
        )
        return self._to_entity(Consoles.objects.get(pk=entity.id))

    def delete(self, id: int) -> None:
        Consoles.objects.filter(pk=id).delete()
