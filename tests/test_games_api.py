"""
Tests for games API v1.
"""

from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestGamesListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/games/")
        assert response.status_code == 200

    def test_returns_paginated_results(self, api_client, game):
        response = api_client.get("/api/v1/games/")
        data = response.json()
        assert "results" in data
        assert data["count"] >= 1

    def test_game_fields(self, api_client, game):
        response = api_client.get("/api/v1/games/")
        result = response.json()["results"][0]
        assert "id" in result
        assert "name" in result
        assert "slug" in result
        assert "release_year" in result

    def test_search_by_name(self, api_client, game):
        response = api_client.get("/api/v1/games/?search=Mario")
        assert response.json()["count"] >= 1

    def test_search_no_match(self, api_client, game):
        response = api_client.get("/api/v1/games/?search=zzznomatch")
        assert response.json()["count"] == 0

    def test_filter_by_genre(self, api_client, game, genre):
        response = api_client.get(f"/api/v1/games/?genre={genre.id}")
        assert response.json()["count"] >= 1

    def test_filter_by_console(self, api_client, game, console):
        response = api_client.get(f"/api/v1/games/?console={console.id}")
        assert response.json()["count"] >= 1

    def test_filter_by_year(self, api_client, game):
        response = api_client.get("/api/v1/games/?year=1985")
        assert response.json()["count"] >= 1

    def test_filter_by_franchise(self, api_client, game, franchise):
        response = api_client.get(f"/api/v1/games/?franchise={franchise.id}")
        assert response.json()["count"] >= 1


@pytest.mark.django_db
class TestGamesDetailEndpoint:
    def test_returns_200(self, api_client, game):
        response = api_client.get(f"/api/v1/games/{game.id}/")
        assert response.status_code == 200

    def test_returns_correct_game(self, api_client, game):
        response = api_client.get(f"/api/v1/games/{game.id}/")
        assert response.json()["name"] == "Super Mario Bros"

    def test_returns_404_for_unknown(self, api_client):
        response = api_client.get("/api/v1/games/00000000-0000-0000-0000-000000000000/")
        assert response.status_code == 404
