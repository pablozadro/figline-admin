#/bin/bash

echo "[+] Loading ingredients fixtures..."
python manage.py loaddata apps/ingredients/fixtures/categories.json
python manage.py loaddata apps/ingredients/fixtures/ingredients.json

echo "[+] Loading recipes fixtures..."
python manage.py loaddata apps/recipes/fixtures/categories.json
python manage.py loaddata apps/recipes/fixtures/recipes.json
python manage.py loaddata apps/recipes/fixtures/ingredients_in_recipes.json
