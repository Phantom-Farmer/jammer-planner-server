#!/bin/bash
rm -rf jammerplannerapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations jammerplannerapi
python manage.py migrate jammerplannerapi
python manage.py loaddata users
python manage.py loaddata bands
python manage.py loaddata songs
python manage.py loaddata sets
python manage.py loaddata set_songs
python manage.py loaddata rehearsals
python manage.py loaddata comments
