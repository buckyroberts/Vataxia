#!/bin/bash

# Accounts
python manage.py loaddata v1/accounts/fixtures/user.json
python manage.py loaddata v1/accounts/fixtures/profile.json
python manage.py loaddata v1/accounts/fixtures/token.json
