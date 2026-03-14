"""
    Repository interfaces for consoles domain.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from apps.consoles.domain.entities import ConsoleEntity


class AbstractConsoleRepository(ABC):
    """Abstract repository for consoles."""

    @abstractmethod
    def list_all(self) -> list[ConsoleEntity]:
        ...

    @abstractmethod
    def get_by_id(self, id: int) -> ConsoleEntity | None:
        ...

    @abstractmethod
    def create(self, entity: ConsoleEntity) -> ConsoleEntity:
        ...

    @abstractmethod
    def update(self, entity: ConsoleEntity) -> ConsoleEntity:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...
