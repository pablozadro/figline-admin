# Overview

## Development environment

In development, Django uses:

- Python development server
- SQLite database for easy and fast development setup and flow


## Settings

Default Settings are set in `project/manage.py`:

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development')
```