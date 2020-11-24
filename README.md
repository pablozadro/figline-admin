# Figline-Admin

Figline-Admin is a Django based app to manage recipes.


## Getting Started

```bash
# setup environment
cp project/.env.example project/.env

# create & activate a virtual environment
python3 -m venv venv
. ./venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# run development server
cd project
python manage.py runserver localhost:9000

# run initial tasks
. ./tasks/db/migrate.sh
. ./tasks/db/load.sh
```


## Docs

- [Overview](/docs/overview.md)
- [Endpoints](/docs/endpoints.md)
