from __future__ import annotations

from rest_framework import serializers

from apps.consoles.infrastructure.models import Consoles


class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consoles
        fields = ("id", "name", "name_en", "name_es", "manufacturer", "release_year", "generation", "type")
