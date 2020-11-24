from decimal import *
from django.test import TestCase
from django.db.utils import IntegrityError
from apps.tools import units
# use full path avoid issues when running the test
from apps.ingredients.models import Ingredient, IngredientCategory


class IngredientModelTest(TestCase):
    
    def setUp(self):
        self.category_a = IngredientCategory.objects.create(title='category A') 
        self.category_b = IngredientCategory.objects.create(title='category B')
    
    def test_title_category_uniqueness(self):
        """Should save two instances with same title only with different category"""
        ingredient_1 = Ingredient.objects.create(title='ingredient 1', category= self.category_a)
        ingredient_2 = Ingredient.objects.create(title= 'ingredient 1', category= self.category_b)
        ingredient_3 = Ingredient(title= 'ingredient 1', category= self.category_b)
        self.assertEqual(ingredient_1.title, ingredient_2.title)
        self.assertRaises(IntegrityError, lambda: ingredient_3.save())
