#/bin/bash

echo "[+] Testing apps..."
python manage.py test apps/units
python manage.py test apps/ingredients --keepdb
python manage.py test apps/recipes --keepdb
