from __future__ import annotations
from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.releases.api.v1.serializers import ReleaseSerializer
from apps.releases.infrastructure.models import Releases

class ReleaseViewSet(ReadOnlyModelViewSet):
    """ViewSet for releases read-only operations."""
    queryset = Releases.objects.select_related("game", "region", "console").all()
    serializer_class = ReleaseSerializer
