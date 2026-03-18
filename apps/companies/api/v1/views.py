"""
    Views for companies API v1.
"""
from __future__ import annotations

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.companies.api.v1.serializers import CompanySerializer
from apps.companies.infrastructure.models import Companies


class CompanyViewSet(ReadOnlyModelViewSet):
    """ViewSet for companies read-only operations."""

    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "country"]
    ordering_fields = ["name", "founded", "country"]
    ordering = ["name"]

    def get_queryset(self):
        qs = super().get_queryset()
        country = self.request.query_params.get("country")
        if country:
            qs = qs.filter(country__icontains=country)
        return qs
