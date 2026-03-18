"""
Tests for regions API v1.
"""

from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestRegionsListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/regions/")
        assert response.status_code == 200

    def test_returns_region(self, api_client, region):
        data = api_client.get("/api/v1/regions/").json()
        assert data["count"] >= 1

    def test_search_by_code(self, api_client, region):
        response = api_client.get("/api/v1/regions/?search=NA")
        assert response.json()["count"] >= 1


@pytest.mark.django_db
class TestRegionsDetailEndpoint:
    def test_returns_200(self, api_client, region):
        response = api_client.get(f"/api/v1/regions/{region.id}/")
        assert response.status_code == 200

    def test_returns_correct_region(self, api_client, region):
        response = api_client.get(f"/api/v1/regions/{region.id}/")
        assert response.json()["code"] == "NA"
