"""
    Serializers for games API v1.
"""
from __future__ import annotations

from rest_framework import serializers

from apps.companies.infrastructure.models import Companies
from apps.consoles.infrastructure.models import Consoles
from apps.games.infrastructure.models import Games
from apps.genres.infrastructure.models import Genres


class GameSerializer(serializers.ModelSerializer):
    """Serializer for the Games model."""

    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genres.objects.all(),
        allow_null=True,
        required=False,
    )
    developer = serializers.PrimaryKeyRelatedField(
        queryset=Companies.objects.all(),
        allow_null=True,
        required=False,
    )
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Companies.objects.all(),
        allow_null=True,
        required=False,
    )
    consoles = serializers.PrimaryKeyRelatedField(
        queryset=Consoles.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Games
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "release_year",
            "genre",
            "developer",
            "publisher",
            "consoles",
        ]
