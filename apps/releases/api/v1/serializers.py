from __future__ import annotations

from rest_framework import serializers

from apps.releases.infrastructure.models import Releases


class ReleaseSerializer(serializers.ModelSerializer):
    game_name = serializers.CharField(source="game.name", read_only=True)
    region_code = serializers.CharField(source="region.code", read_only=True)
    region_name = serializers.CharField(source="region.name", read_only=True)
    console_name = serializers.CharField(source="console.name", read_only=True, allow_null=True)

    class Meta:
        model = Releases
        fields = (
            "id",
            "game",
            "game_name",
            "region",
            "region_code",
            "region_name",
            "console",
            "console_name",
            "release_date",
        )
