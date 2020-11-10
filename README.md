## Prerequisite
- Docker
- docker-compose
- python >= 3.8
- poetry >= 1.1.4

## Install dependencies

This project uses `poetry` as its package manager. To install dependencies, run

```
poetry install
```

## Development

### poetry

Activate `poetry` env first

```
poetry shell
```

### Production:
export DJANGO_SETTINGS_MODULE=base.settings.production

### Development:

export DJANGO_SETTINGS_MODULE=base.settings.dev


### Start dev
```
cp .env.example .env
docker-compose up -d
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
```

### Start celery worker / beat
```
celery -A base worker --beat -l info
```

### Test
```
./manage.py test
```

## heroku deploy 
```
heroku create
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set DJANGO_SETTINGS_MODULE=base.settings.heroku
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open
```