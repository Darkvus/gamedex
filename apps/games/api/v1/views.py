"""
    Views for games API v1.
"""
from __future__ import annotations

from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.games.api.v1.serializers import GameSerializer
from apps.games.infrastructure.models import Games


class GameViewSet(ReadOnlyModelViewSet):
    """ViewSet for games read-only operations."""

    queryset = (
        Games.objects.select_related("genre", "developer", "publisher")
        .prefetch_related("consoles")
        .all()
    )
    serializer_class = GameSerializer
