"""
    Serializers for genres API v1.
"""
from __future__ import annotations

from rest_framework import serializers

from apps.genres.infrastructure.models import Genres


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the Genres model."""

    class Meta:
        model = Genres
        fields = ["id", "name", "description"]
