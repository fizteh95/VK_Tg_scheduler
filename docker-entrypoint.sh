#!/bin/sh

alembic upgrade head
python manage.py run
