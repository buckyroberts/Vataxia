![](http://i.imgur.com/Da1hAJS.png)

## Project Setup

Install required packages:
```
pip3 install -r requirements/local.txt
```

Initialize database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Fixtures

To load in sample data for all tables at once:
```
bash scripts/load_sample_data.sh
```

This will create an initial superuser account with the following credentials:
```
admin@email.com
pass1234
```
