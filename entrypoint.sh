#!/bin/sh
set -e

python manage.py migrate --noinput

python manage.py loaddata \
  apps/genres/fixtures/genres.json \
  apps/companies/fixtures/companies.json \
  apps/consoles/fixtures/consoles.json \
  apps/games/fixtures/games.json \
  apps/regions/fixtures/regions.json \
  apps/releases/fixtures/releases.json

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
