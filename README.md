### Production:
export DJANGO_SETTINGS_MODULE=backend.settings.production

### Development:

export DJANGO_SETTINGS_MODULE=backend.settings.dev

#### Bash
```
if [ -f "$PWD/venv/bin/activate" ]; then
    source "$PWD/venv/bin/activate"
fi
```