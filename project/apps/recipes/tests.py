from decimal import *
from django.test import TestCase
from django.db.utils import IntegrityError
from apps.tools import units
from apps.ingredients.models import IngredientCategory, Ingredient
# use full path avoid issues when running the test
from apps.recipes.models import RecipeCategory, Recipe, IngredientInRecipe


class RecipeModelTest(TestCase):

    def setUp(self):
        # Categories
        self.category_a = RecipeCategory.objects.create(title="category A")
        self.category_b = RecipeCategory.objects.create(title="category B")
        self.category_c = RecipeCategory.objects.create(title= "category C")

        # Ingredients
        self.ingredient_1 = Ingredient.objects.create(
            title='ingredient 1', 
            price_value= 60, 
            price_unit= units.LT
        )

        self.ingredient_2 = Ingredient.objects.create(
            title='ingredient 2', 
            price_value= 40, 
            price_unit= units.KG
        )

        self.ingredient_3 = Ingredient.objects.create(
            title='ingredient 3', 
            price_value= 500, 
            price_unit= units.KG
        )

        self.ingredient_4 = Ingredient.objects.create(
            title='ingredient 4', 
            price_value= 700, 
            price_unit= units.KG
        )

        self.ingredient_5 = Ingredient.objects.create(
            title='ingredient 5', 
            price_value= 1, 
            price_unit= units.UN
        )

        self.ingredient_6 = Ingredient.objects.create(
            title='ingredient 6', 
            price_value= 700, 
            price_unit= units.KG
        )


        # Recipes
        self.recipe_1 = Recipe.objects.create(
            title="recipe 1", 
            category=self.category_a, 
            portion_size= Decimal('1120.00'), 
            portion_unit= units.ML
        ) 

        IngredientInRecipe.objects.create(
            recipe=self.recipe_1, 
            ingredient=self.ingredient_1, 
            amount=1000, 
            unit=units.ML
        ) # cost: 60

        IngredientInRecipe.objects.create(
            recipe=self.recipe_1, 
            ingredient=self.ingredient_2, 
            amount=60, 
            unit=units.GR
        ) # cost: 2.4

        IngredientInRecipe.objects.create(
            recipe=self.recipe_1, 
            ingredient=self.ingredient_3, 
            amount=60, 
            unit=units.GR
        ) # cost: 30

        IngredientInRecipe.objects.create(
            recipe=self.recipe_1, 
            ingredient=self.ingredient_4, 
            unit=units.CN
        ) # cost: 0

        IngredientInRecipe.objects.create(
            recipe=self.recipe_1, 
            ingredient=self.ingredient_5,
            amount=2, 
            unit=units.UN, 
            optional=True
        ) # cost: 2
        
        # Mornay: cost: 82.5 | 1.78 | 84.28
        self.recipe_2 = Recipe.objects.create(
            title="recipe 2", 
            category=self.category_b,
            portion_size= Decimal('1125.00'), 
            portion_unit= units.ML
        ) 
        IngredientInRecipe.objects.create(
            recipe=self.recipe_2, 
            ingredient=self.ingredient_6, 
            amount=125, 
            unit=units.GR
        ) 
        
    
    def test_recipe_title_category_uniqueness_save(self):
        recipe1 = Recipe.objects.create(title="foo recipe", category=self.category_a)
        recipe2 = Recipe.objects.create(title="foo recipe", category=self.category_b)
        recipe3 = Recipe(title="foo recipe", category=self.category_a)
        self.assertEqual( recipe1.title, recipe2.title)
        self.assertRaises( IntegrityError, lambda: recipe3.save())

    def test_ingredients(self):
        """Should return the ingredients properly"""
        self.assertEqual( len(self.recipe_1.ingredients), 5)
    
    def test_costs(self):
        """Should test the costs for the recipe"""
        self.assertEqual( self.recipe_1.costs['base'], Decimal('92.40'))
        self.assertEqual( self.recipe_1.costs['optionals'], Decimal('2'))
        self.assertEqual( self.recipe_1.costs['total'], Decimal('94.40'))

    def test_calculate_by_portion_size(self):
        """Should test all the required calculations for given portion"""
        # TODO: how tot test that?
        for related in self.recipe_1.ingredients:
            print("{} / {}".format(related.ingredient.title, related.amount))        
        self.recipe_1.calculate(portion=Decimal('560.00'))
        for related in self.recipe_1.ingredients:
            print("{} / {}".format(related.ingredient.title, related.amount))        
        


class IngredientInRecipeTest(TestCase):
    
    def setUp(self):
        pass

    def test_recipe_ingredient_uniqueness_save(self):
        """Should not save the same recipe/ingredient twice"""
        recipe = Recipe.objects.create(title="recipe 1")
        ingredient = Ingredient.objects.create(title='ingredient 1')
        IngredientInRecipe.objects.create(recipe=recipe, ingredient=ingredient)
        x = IngredientInRecipe(recipe=recipe, ingredient=ingredient)
        self.assertRaises( IntegrityError, lambda: x.save())

    def test_wrong_unit(self):
        """Should raise an error if the unit is not valid"""
        recipe = Recipe.objects.create(title="recipe 1")
        ingredient = Ingredient.objects.create(title='ingredient 1')
        x = IngredientInRecipe(recipe=recipe, ingredient=ingredient, amount=2, unit = units.KG)
        self.assertRaises( ValueError, lambda: x.save())

    def test_cost(self):      
        """Should test the cost of and ingredient in given recipe"""
        leche = Ingredient.objects.create(title='leche', price = 100, unit = units.LT)
        moscada = Ingredient.objects.create(title='moscada', price = 100, unit = units.LT)
        clavo_olor = Ingredient.objects.create(title='clavo de olor', price = 1, unit = units.UN)
        bechamel = Recipe.objects.create(title='bechamel') 
        leche_in_bechamel = IngredientInRecipe(recipe=bechamel, ingredient=leche, amount=500, unit=units.ML)
        moscada_in_bechamel = IngredientInRecipe(recipe=bechamel, ingredient=moscada, unit=units.CN)
        self.assertEqual(leche_in_bechamel.cost, leche.get_price(amount=500, unit=units.ML))
        self.assertEqual(moscada_in_bechamel.cost, 0)
