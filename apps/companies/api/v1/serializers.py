from __future__ import annotations

from rest_framework import serializers

from apps.companies.infrastructure.models import Companies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ("id", "name", "name_en", "name_es", "country", "founded", "website")
