#!/bin/bash

# Accounts
python3 manage.py loaddata v1/accounts/fixtures/user.json
python3 manage.py loaddata v1/accounts/fixtures/profile.json
python3 manage.py loaddata v1/accounts/fixtures/token.json

# User roles
python3 manage.py loaddata v1/user_roles/fixtures/administrator.json
python3 manage.py loaddata v1/user_roles/fixtures/moderator.json
