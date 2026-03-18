from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.releases.api.v1.serializers import ReleaseSerializer
from apps.releases.infrastructure.models import Releases


class ReleaseViewSet(ReadOnlyModelViewSet):
    """ViewSet for releases read-only operations."""

    queryset = Releases.objects.select_related("game", "region", "console").all()
    serializer_class = ReleaseSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["game__name", "region__name", "region__code"]
    ordering_fields = ["release_date", "game__name"]
    ordering = ["release_date"]

    def get_queryset(self):
        qs = super().get_queryset()
        game = self.request.query_params.get("game")
        region = self.request.query_params.get("region")
        console = self.request.query_params.get("console")
        if game:
            qs = qs.filter(game_id=game)
        if region:
            qs = qs.filter(region_id=region)
        if console:
            qs = qs.filter(console_id=console)
        return qs
