from __future__ import annotations

from rest_framework import serializers

from apps.games.infrastructure.models import Games


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = (
            "id", "name", "name_en", "name_es",
            "slug", "description", "description_en", "description_es",
            "release_year", "genre", "developer", "publisher", "consoles",
        )
