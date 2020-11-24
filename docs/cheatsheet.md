# Cheatsheet


## Python & Pip

```bash
python3 -m venv venv
. ./venv/bin/activate

pip install python-decouple markdown django django-filter django-debug-toolbar djangorestframework
pip freeze > requirements.txt
pip install -r requirements.txt
```


## Project

```bash
# Server
python manage.py runserver

# Migrations
python manage.py makemigrations {app}
python manage.py migrate {app}

# Dump & Load data
python manage.py dumpdata {app}.{model} --indent=2 --output=apps/{app}/fixtures/{filename}.json 
python manage.py loaddata apps/{app}/fixtures/{filename}.json
```


# UI

```bash
cd project/ui
npm link core-radio
npm install
npm run scss:watch
npm run js:watch
```


# Docker

```bash
docker image ls -a # list all images
docker container ls -a # list all containers
docker-compose up --build {service}
docker exec -it {container} bash # enter container
```