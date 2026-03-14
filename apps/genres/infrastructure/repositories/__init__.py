"""
    Django ORM repository implementation for genres.
"""
from __future__ import annotations

from apps.genres.domain.entities import GenreEntity
from apps.genres.domain.repositories import AbstractGenreRepository
from apps.genres.infrastructure.models import Genres


class DjangoGenreRepository(AbstractGenreRepository):
    """Django ORM implementation of the genre repository."""

    def _to_entity(self, obj: Genres) -> GenreEntity:
        return GenreEntity(id=obj.pk, name=obj.name, description=obj.description)

    def list_all(self) -> list[GenreEntity]:
        return [self._to_entity(obj) for obj in Genres.objects.all()]

    def get_by_id(self, id: int) -> GenreEntity | None:
        try:
            return self._to_entity(Genres.objects.get(pk=id))
        except Genres.DoesNotExist:
            return None

    def create(self, entity: GenreEntity) -> GenreEntity:
        obj = Genres.objects.create(name=entity.name, description=entity.description)
        return self._to_entity(obj)

    def update(self, entity: GenreEntity) -> GenreEntity:
        Genres.objects.filter(pk=entity.id).update(
            name=entity.name, description=entity.description
        )
        return self._to_entity(Genres.objects.get(pk=entity.id))

    def delete(self, id: int) -> None:
        Genres.objects.filter(pk=id).delete()
