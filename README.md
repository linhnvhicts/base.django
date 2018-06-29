### Production:
export DJANGO_SETTINGS_MODULE=base.settings.production

### Development:

export DJANGO_SETTINGS_MODULE=base.settings.dev

#### Bash
```
if [ -f "$PWD/venv/bin/activate" ]; then
    source "$PWD/venv/bin/activate"
fi
```

#### heroku deploy 
heroku create

heroku config:set DISABLE_COLLECTSTATIC=1

heroku config:set DJANGO_SETTINGS_MODULE=base.settings.heroku

git push heroku master

heroku run python manage.py migrate

heroku run python manage.py createsuperuser

heroku open

### Docker:

#### Prerequisite
Docker version 18.03.1-ce, build 9ee9f40
docker-compose version 1.21.1, build 5a3f1a3

#### Start dev
cp .env.example .env
docker-compose up
docker-compose exec web python3 manage.py migrate
docker-compose exec web python3 manage.py createsuperuser