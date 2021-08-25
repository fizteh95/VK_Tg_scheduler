#!/bin/sh

flask db upgrade
python manage.py run
