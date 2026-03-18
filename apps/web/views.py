from __future__ import annotations

from inertia import render

from apps.consoles.infrastructure.models import Consoles
from apps.games.infrastructure.models import Games
from apps.genres.infrastructure.models import Genres


def _serialize_game(game: Games) -> dict:
    return {
        "id": str(game.id),
        "name": game.name,
        "slug": game.slug,
        "description": game.description or "",
        "release_year": game.release_year,
        "genre": {"id": str(game.genre.id), "name": game.genre.name} if game.genre else None,
        "developer": {"id": str(game.developer.id), "name": game.developer.name} if game.developer else None,
        "publisher": {"id": str(game.publisher.id), "name": game.publisher.name} if game.publisher else None,
        "consoles": [{"id": str(c.id), "name": c.name} for c in game.consoles.all()],
        "cover_url": game.cover_url or "",
    }


def catalog(request):
    genre_id = request.GET.get("genre", "")
    console_id = request.GET.get("console", "")
    year = request.GET.get("year", "")
    search = request.GET.get("search", "")

    qs = (
        Games.objects.select_related("genre", "developer", "publisher")
        .prefetch_related("consoles")
        .all()
    )
    if genre_id:
        qs = qs.filter(genre_id=genre_id)
    if console_id:
        qs = qs.filter(consoles__id=console_id).distinct()
    if year:
        qs = qs.filter(release_year=year)
    if search:
        qs = qs.filter(name__icontains=search)

    years = (
        Games.objects.exclude(release_year=None)
        .values_list("release_year", flat=True)
        .distinct()
        .order_by("-release_year")
    )

    return render(request, "Catalog", props={
        "games": [_serialize_game(g) for g in qs],
        "genres": [{"id": str(g.id), "name": g.name} for g in Genres.objects.all()],
        "consoles": [{"id": str(c.id), "name": c.name} for c in Consoles.objects.order_by("name")],
        "years": list(years),
        "filters": {"genre": genre_id, "console": console_id, "year": year, "search": search},
    })


def collection(request):
    qs = (
        Games.objects.select_related("genre", "developer", "publisher")
        .prefetch_related("consoles")
        .all()
    )
    return render(request, "Collection", props={
        "games": [_serialize_game(g) for g in qs],
    })


def game_detail(request, slug: str):
    game = (
        Games.objects.select_related("genre", "developer", "publisher")
        .prefetch_related("consoles")
        .get(slug=slug)
    )
    data = _serialize_game(game)
    data["releases"] = [
        {
            "id": str(r.id),
            "region": {"code": r.region.code, "name": r.region.name},
            "console": {"name": r.console.name} if r.console else None,
            "release_date": r.release_date.isoformat() if r.release_date else None,
        }
        for r in game.releases.select_related("region", "console").order_by("release_date")
    ]
    return render(request, "GameDetail", props={"game": data})


def api_explorer(request):
    endpoints = [
        {
            "group": "Games",
            "color": "red",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/games/",
                    "description": "Returns a paginated list of all games in the catalog.",
                    "params": [
                        {"name": "page", "type": "integer", "required": False, "description": "Page number (default: 1)"},
                        {"name": "page_size", "type": "integer", "required": False, "description": "Results per page"},
                        {"name": "search", "type": "string", "required": False, "description": "Search by name or description"},
                        {"name": "genre", "type": "uuid", "required": False, "description": "Filter by genre ID"},
                        {"name": "console", "type": "uuid", "required": False, "description": "Filter by console ID"},
                        {"name": "year", "type": "integer", "required": False, "description": "Filter by release year"},
                        {"name": "franchise", "type": "uuid", "required": False, "description": "Filter by franchise ID"},
                        {"name": "developer", "type": "uuid", "required": False, "description": "Filter by developer ID"},
                        {"name": "publisher", "type": "uuid", "required": False, "description": "Filter by publisher ID"},
                        {"name": "ordering", "type": "string", "required": False, "description": "Sort by: name, release_year, -name, -release_year"},
                    ],
                    "example_response": '{"count":150,"next":"/api/v1/games/?page=2","results":[{"id":"...","name":"Super Mario Bros","slug":"super-mario-bros","release_year":1985,"genre":"...","developer":"..."}]}',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/games/{id}/",
                    "description": "Returns a single game by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Game UUID identifier"},
                    ],
                    "example_response": '{"id":"44444444-0000-0000-0000-000000000001","name":"Super Mario Bros","slug":"super-mario-bros","release_year":1985,"genre":"11111111-...","consoles":["33333333-..."]}',
                },
            ],
        },
        {
            "group": "Genres",
            "color": "purple",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/genres/",
                    "description": "Returns the list of all game genres.",
                    "params": [],
                    "example_response": '[{"id":"11111111-0000-0000-0000-000000000001","name":"Action","description":"Fast-paced games focused on physical challenges."}]',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/genres/{id}/",
                    "description": "Returns a single genre by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Genre UUID identifier"},
                    ],
                    "example_response": '{"id":"11111111-0000-0000-0000-000000000001","name":"Action","name_en":"Action","name_es":"Acción","description":"..."}',
                },
            ],
        },
        {
            "group": "Consoles",
            "color": "blue",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/consoles/",
                    "description": "Returns the list of all gaming platforms.",
                    "params": [],
                    "example_response": '[{"id":"33333333-...","name":"NES","manufacturer":"Nintendo","release_year":1983,"generation":3,"type":"home"}]',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/consoles/{id}/",
                    "description": "Returns a single console by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Console UUID identifier"},
                    ],
                    "example_response": '{"id":"33333333-0000-0000-0000-000000000022","name":"PlayStation 5","manufacturer":"Sony Interactive Entertainment","release_year":2020,"generation":9,"type":"home"}',
                },
            ],
        },
        {
            "group": "Companies",
            "color": "yellow",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/companies/",
                    "description": "Returns the list of all publishers and developers.",
                    "params": [],
                    "example_response": '[{"id":"22222222-...","name":"Nintendo","country":"Japan","founded":1889,"website":"https://www.nintendo.com"}]',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/companies/{id}/",
                    "description": "Returns a single company by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Company UUID identifier"},
                    ],
                    "example_response": '{"id":"22222222-0000-0000-0000-000000000001","name":"Nintendo","name_en":"Nintendo","country":"Japan","founded":1889,"website":"https://www.nintendo.com"}',
                },
            ],
        },
        {
            "group": "Regions",
            "color": "green",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/regions/",
                    "description": "Returns the list of release regions.",
                    "params": [
                        {"name": "search", "type": "string", "required": False, "description": "Search by code or name"},
                        {"name": "ordering", "type": "string", "required": False, "description": "Sort by: code, name"},
                    ],
                    "example_response": '[{"id":"77777777-...","code":"NA","name":"North America"},{"id":"77777777-...","code":"EU","name":"Europe"}]',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/regions/{id}/",
                    "description": "Returns a single region by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Region UUID identifier"},
                    ],
                    "example_response": '{"id":"77777777-0000-0000-0000-000000000001","code":"JP","name":"Japan","name_en":"Japan","name_es":"Japón"}',
                },
            ],
        },
        {
            "group": "Releases",
            "color": "orange",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/releases/",
                    "description": "Returns game release records with region, console and date.",
                    "params": [
                        {"name": "game", "type": "uuid", "required": False, "description": "Filter by game ID"},
                        {"name": "region", "type": "uuid", "required": False, "description": "Filter by region ID"},
                        {"name": "console", "type": "uuid", "required": False, "description": "Filter by console ID"},
                        {"name": "search", "type": "string", "required": False, "description": "Search by game name or region"},
                        {"name": "ordering", "type": "string", "required": False, "description": "Sort by: release_date, game__name"},
                    ],
                    "example_response": '[{"id":"55555555-...","game":"44444444-...","game_name":"Super Mario Bros","region_code":"JP","console_name":"NES","release_date":"1983-07-14"}]',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/releases/{id}/",
                    "description": "Returns a single release record by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Release UUID identifier"},
                    ],
                    "example_response": '{"id":"55555555-0000-0000-0000-000000000001","game":"44444444-...","game_name":"Super Mario Bros","region_code":"JP","region_name":"Japan","console_name":"NES","release_date":"1983-07-14"}',
                },
            ],
        },
        {
            "group": "Franchises",
            "color": "pink",
            "endpoints": [
                {
                    "method": "GET",
                    "path": "/api/v1/franchises/",
                    "description": "Returns the list of all game franchises/series.",
                    "params": [
                        {"name": "search", "type": "string", "required": False, "description": "Search by name or description"},
                        {"name": "ordering", "type": "string", "required": False, "description": "Sort by: name, founded_year"},
                    ],
                    "example_response": '[{"id":"66666666-...","name":"Super Mario","slug":"super-mario","founded_year":1985,"games_count":15}]',
                },
                {
                    "method": "GET",
                    "path": "/api/v1/franchises/{id}/",
                    "description": "Returns a single franchise by its UUID.",
                    "params": [
                        {"name": "id", "type": "uuid", "required": True, "description": "Franchise UUID identifier"},
                    ],
                    "example_response": '{"id":"66666666-0000-0000-0000-000000000001","name":"Super Mario","slug":"super-mario","description":"The Super Mario franchise...","founded_year":1985,"games_count":15}',
                },
            ],
        },
    ]
    return render(request, "ApiExplorer", props={"endpoints": endpoints})
