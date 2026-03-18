"""
Views for consoles API v1.
"""

from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.consoles.api.v1.serializers import ConsoleSerializer
from apps.consoles.infrastructure.models import Consoles


class ConsoleViewSet(ReadOnlyModelViewSet):
    """ViewSet for consoles read-only operations."""

    queryset = Consoles.objects.all()
    serializer_class = ConsoleSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "manufacturer"]
    ordering_fields = ["name", "release_year", "generation"]
    ordering = ["name"]

    def get_queryset(self):
        qs = super().get_queryset()
        generation = self.request.query_params.get("generation")
        console_type = self.request.query_params.get("type")
        manufacturer = self.request.query_params.get("manufacturer")
        if generation:
            qs = qs.filter(generation=generation)
        if console_type:
            qs = qs.filter(type=console_type)
        if manufacturer:
            qs = qs.filter(manufacturer__icontains=manufacturer)
        return qs
