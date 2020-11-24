#/bin/bash

echo "[+] Dumping ingredients fixtures..."
python manage.py dumpdata ingredients.IngredientCategory --indent=2 --output=apps/ingredients/fixtures/categories.json
python manage.py dumpdata ingredients.Ingredient --indent=2 --output=apps/ingredients/fixtures/ingredients.json

echo "[+] Dumping recipes fixtures..."
python manage.py dumpdata recipes.RecipeCategory --indent=2 --output=apps/recipes/fixtures/categories.json
python manage.py dumpdata recipes.Recipe --indent=2 --output=apps/recipes/fixtures/recipes.json
python manage.py dumpdata recipes.IngredientInRecipe --indent=2 --output=apps/recipes/fixtures/ingredients_in_recipes.json
