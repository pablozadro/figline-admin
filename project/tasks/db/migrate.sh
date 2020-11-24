#/bin/bash

echo "[+] Migrating Django apps..."
python manage.py migrate

echo "[+] Migrating Own apps..."
python manage.py migrate ingredients
python manage.py migrate recipes

