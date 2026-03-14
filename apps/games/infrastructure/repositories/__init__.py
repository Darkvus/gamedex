"""
    Django ORM repository implementation for games.
"""
from __future__ import annotations

from apps.games.domain.entities import GameEntity
from apps.games.domain.repositories import AbstractGameRepository
from apps.games.infrastructure.models import Games


class DjangoGameRepository(AbstractGameRepository):
    """Django ORM implementation of the game repository."""

    def _to_entity(self, obj: Games) -> GameEntity:
        return GameEntity(
            id=obj.pk,
            name=obj.name,
            slug=obj.slug,
            description=obj.description,
            release_year=obj.release_year,
            genre_id=obj.genre_id,
            developer_id=obj.developer_id,
            publisher_id=obj.publisher_id,
        )

    def list_all(self) -> list[GameEntity]:
        return [self._to_entity(obj) for obj in Games.objects.all()]

    def get_by_id(self, id: int) -> GameEntity | None:
        try:
            return self._to_entity(Games.objects.get(pk=id))
        except Games.DoesNotExist:
            return None

    def create(self, entity: GameEntity) -> GameEntity:
        obj = Games.objects.create(
            name=entity.name,
            slug=entity.slug,
            description=entity.description,
            release_year=entity.release_year,
            genre_id=entity.genre_id,
            developer_id=entity.developer_id,
            publisher_id=entity.publisher_id,
        )
        return self._to_entity(obj)

    def update(self, entity: GameEntity) -> GameEntity:
        Games.objects.filter(pk=entity.id).update(
            name=entity.name,
            slug=entity.slug,
            description=entity.description,
            release_year=entity.release_year,
            genre_id=entity.genre_id,
            developer_id=entity.developer_id,
            publisher_id=entity.publisher_id,
        )
        return self._to_entity(Games.objects.get(pk=entity.id))

    def delete(self, id: int) -> None:
        Games.objects.filter(pk=id).delete()
