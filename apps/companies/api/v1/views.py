"""
    Views for companies API v1.
"""
from __future__ import annotations

from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.companies.api.v1.serializers import CompanySerializer
from apps.companies.infrastructure.models import Companies


class CompanyViewSet(ReadOnlyModelViewSet):
    """ViewSet for companies read-only operations."""

    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
