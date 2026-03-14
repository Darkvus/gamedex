"""
    Serializers for companies API v1.
"""
from __future__ import annotations

from rest_framework import serializers

from apps.companies.infrastructure.models import Companies


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for the Companies model."""

    class Meta:
        model = Companies
        fields = ["id", "name", "country", "founded", "website"]
