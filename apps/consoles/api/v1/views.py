"""
    Views for consoles API v1.
"""
from __future__ import annotations

from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.consoles.api.v1.serializers import ConsoleSerializer
from apps.consoles.infrastructure.models import Consoles


class ConsoleViewSet(ReadOnlyModelViewSet):
    """ViewSet for consoles read-only operations."""

    queryset = Consoles.objects.all()
    serializer_class = ConsoleSerializer
