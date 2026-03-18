"""
Repository interfaces for games domain.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from apps.games.domain.entities import GameEntity


class AbstractGameRepository(ABC):
    """Abstract repository for games."""

    @abstractmethod
    def list_all(self) -> list[GameEntity]: ...

    @abstractmethod
    def get_by_id(self, id: int) -> GameEntity | None: ...

    @abstractmethod
    def create(self, entity: GameEntity) -> GameEntity: ...

    @abstractmethod
    def update(self, entity: GameEntity) -> GameEntity: ...

    @abstractmethod
    def delete(self, id: int) -> None: ...
