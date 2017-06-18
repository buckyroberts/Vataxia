#!/bin/bash

# Accounts
python3 manage.py loaddata v1/accounts/fixtures/user.json
python3 manage.py loaddata v1/accounts/fixtures/profile.json
python3 manage.py loaddata v1/accounts/fixtures/token.json
