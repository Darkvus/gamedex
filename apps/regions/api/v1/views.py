from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.regions.api.v1.serializers import RegionSerializer
from apps.regions.infrastructure.models import Regions


class RegionViewSet(ReadOnlyModelViewSet):
    """ViewSet for regions read-only operations."""

    queryset = Regions.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "code"]
    ordering_fields = ["code", "name"]
    ordering = ["code"]
