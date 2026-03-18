"""
    Serializers for franchises API v1.
"""
from __future__ import annotations

from rest_framework import serializers

from apps.franchises.infrastructure.models import Franchises


class FranchiseSerializer(serializers.ModelSerializer):
    games_count = serializers.SerializerMethodField()

    class Meta:
        model = Franchises
        fields = ("id", "name", "name_en", "name_es", "slug", "description", "description_en", "description_es", "founded_year", "games_count")

    def get_games_count(self, obj: Franchises) -> int:
        return obj.games.count()
