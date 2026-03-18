"""
Tests for releases API v1.
"""

from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestReleasesListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/releases/")
        assert response.status_code == 200

    def test_returns_release(self, api_client, release):
        data = api_client.get("/api/v1/releases/").json()
        assert data["count"] >= 1

    def test_release_fields(self, api_client, release):
        result = api_client.get("/api/v1/releases/").json()["results"][0]
        assert "game_name" in result
        assert "region_code" in result
        assert "console_name" in result
        assert "release_date" in result

    def test_filter_by_game(self, api_client, release, game):
        response = api_client.get(f"/api/v1/releases/?game={game.id}")
        assert response.json()["count"] >= 1

    def test_filter_by_region(self, api_client, release, region):
        response = api_client.get(f"/api/v1/releases/?region={region.id}")
        assert response.json()["count"] >= 1


@pytest.mark.django_db
class TestReleasesDetailEndpoint:
    def test_returns_200(self, api_client, release):
        response = api_client.get(f"/api/v1/releases/{release.id}/")
        assert response.status_code == 200
