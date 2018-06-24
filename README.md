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
