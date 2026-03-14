from __future__ import annotations

from rest_framework import serializers

from apps.genres.infrastructure.models import Genres


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ("id", "name", "name_en", "name_es", "description", "description_en", "description_es")
