"""
    Serializers for consoles API v1.
"""
from __future__ import annotations

from rest_framework import serializers

from apps.consoles.infrastructure.models import Consoles


class ConsoleSerializer(serializers.ModelSerializer):
    """Serializer for the Consoles model."""

    class Meta:
        model = Consoles
        fields = ["id", "name", "manufacturer", "release_year", "generation", "type"]
