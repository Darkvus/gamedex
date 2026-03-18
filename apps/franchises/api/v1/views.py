"""
    Views for franchises API v1.
"""
from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.franchises.api.v1.serializers import FranchiseSerializer
from apps.franchises.infrastructure.models import Franchises


class FranchiseViewSet(ReadOnlyModelViewSet):
    """ViewSet for franchises read-only operations."""

    queryset = Franchises.objects.prefetch_related("games").all()
    serializer_class = FranchiseSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "founded_year"]
    ordering = ["name"]
