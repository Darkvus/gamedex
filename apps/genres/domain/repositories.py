"""
    Repository interfaces for genres domain.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from apps.genres.domain.entities import GenreEntity


class AbstractGenreRepository(ABC):
    """Abstract repository for genres."""

    @abstractmethod
    def list_all(self) -> list[GenreEntity]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> GenreEntity | None:
        ...

    @abstractmethod
    def create(self, entity: GenreEntity) -> GenreEntity:
        ...

    @abstractmethod
    def update(self, entity: GenreEntity) -> GenreEntity:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...
