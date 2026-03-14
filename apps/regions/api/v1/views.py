from __future__ import annotations
from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.regions.api.v1.serializers import RegionSerializer
from apps.regions.infrastructure.models import Regions

class RegionViewSet(ReadOnlyModelViewSet):
    """ViewSet for regions read-only operations."""
    queryset = Regions.objects.all()
    serializer_class = RegionSerializer
