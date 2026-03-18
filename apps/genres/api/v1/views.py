"""
    Views for genres API v1.
"""
from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.genres.api.v1.serializers import GenreSerializer
from apps.genres.infrastructure.models import Genres


class GenreViewSet(ReadOnlyModelViewSet):
    """ViewSet for genres read-only operations."""

    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name"]
    ordering = ["name"]
