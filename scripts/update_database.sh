#!/bin/bash


echo 2 | python manage.py makemigrations > ./scripts/output.txt
expect ./scripts/handle_migration_prompt.sh "'Pasadena'"
python manage.py migrate
