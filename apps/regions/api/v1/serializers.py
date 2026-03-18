from __future__ import annotations

from rest_framework import serializers

from apps.regions.infrastructure.models import Regions


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ("id", "code", "name", "name_en", "name_es")
