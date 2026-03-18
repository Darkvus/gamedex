"""
    Tests for franchises API v1.
"""
from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestFranchisesListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/franchises/")
        assert response.status_code == 200

    def test_returns_franchise(self, api_client, franchise):
        data = api_client.get("/api/v1/franchises/").json()
        assert data["count"] >= 1

    def test_franchise_fields(self, api_client, franchise):
        result = api_client.get("/api/v1/franchises/").json()["results"][0]
        assert "id" in result
        assert "name" in result
        assert "slug" in result
        assert "founded_year" in result
        assert "games_count" in result

    def test_search_by_name(self, api_client, franchise):
        response = api_client.get("/api/v1/franchises/?search=Mario")
        assert response.json()["count"] >= 1

    def test_games_count_with_game(self, api_client, game, franchise):
        result = api_client.get(f"/api/v1/franchises/{franchise.id}/").json()
        assert result["games_count"] == 1


@pytest.mark.django_db
class TestFranchisesDetailEndpoint:
    def test_returns_200(self, api_client, franchise):
        response = api_client.get(f"/api/v1/franchises/{franchise.id}/")
        assert response.status_code == 200

    def test_returns_404(self, api_client):
        response = api_client.get("/api/v1/franchises/00000000-0000-0000-0000-000000000000/")
        assert response.status_code == 404
