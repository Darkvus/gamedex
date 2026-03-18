"""
    Tests for companies API v1.
"""
from __future__ import annotations

import pytest


@pytest.mark.django_db
class TestCompaniesListEndpoint:
    def test_returns_200(self, api_client):
        response = api_client.get("/api/v1/companies/")
        assert response.status_code == 200

    def test_returns_company(self, api_client, company):
        data = api_client.get("/api/v1/companies/").json()
        assert data["count"] >= 1

    def test_search_by_name(self, api_client, company):
        response = api_client.get("/api/v1/companies/?search=Nintendo")
        assert response.json()["count"] >= 1

    def test_filter_by_country(self, api_client, company):
        response = api_client.get("/api/v1/companies/?country=Japan")
        assert response.json()["count"] >= 1


@pytest.mark.django_db
class TestCompaniesDetailEndpoint:
    def test_returns_200(self, api_client, company):
        response = api_client.get(f"/api/v1/companies/{company.id}/")
        assert response.status_code == 200

    def test_returns_correct_company(self, api_client, company):
        response = api_client.get(f"/api/v1/companies/{company.id}/")
        assert response.json()["name"] == "Nintendo"
