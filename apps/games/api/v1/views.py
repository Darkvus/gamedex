"""
    Views for games API v1.
"""
from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.games.api.v1.serializers import GameSerializer
from apps.games.infrastructure.models import Games


class GameViewSet(ReadOnlyModelViewSet):
    """ViewSet for games read-only operations."""

    queryset = (
        Games.objects.select_related("genre", "developer", "publisher", "franchise")
        .prefetch_related("consoles")
        .all()
    )
    serializer_class = GameSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "release_year"]
    ordering = ["name"]

    def get_queryset(self):
        qs = super().get_queryset()
        genre = self.request.query_params.get("genre")
        console = self.request.query_params.get("console")
        year = self.request.query_params.get("year")
        franchise = self.request.query_params.get("franchise")
        developer = self.request.query_params.get("developer")
        publisher = self.request.query_params.get("publisher")
        if genre:
            qs = qs.filter(genre_id=genre)
        if console:
            qs = qs.filter(consoles__id=console).distinct()
        if year:
            qs = qs.filter(release_year=year)
        if franchise:
            qs = qs.filter(franchise_id=franchise)
        if developer:
            qs = qs.filter(developer_id=developer)
        if publisher:
            qs = qs.filter(publisher_id=publisher)
        return qs
