from decimal import *
from django.db import models

from apps.tools import units
from apps.ingredients.models import Ingredient
from .managers import RecipeManager


class RecipeCategory(models.Model):

    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "recipes_categories"
        verbose_name = "category"
        verbose_name_plural = "categories"


class Recipe(models.Model):

    PORTION_UNITS = (
        units.GR,
        units.ML,
        units.UN,
        units.NA,
    )
    
    PORTION_UNIT_CHOICES = (
        (PORTION_UNITS[0], 'gr'),
        (PORTION_UNITS[1], 'ml'),
        (PORTION_UNITS[2], 'un'),
        (PORTION_UNITS[3], 'n/a'),
    )    

    title = models.CharField(
        db_index = True, 
        max_length = 100
    )    
    
    category = models.ForeignKey(
        RecipeCategory,
        related_name = "recipes",
        on_delete = models.PROTECT
    )    

    portion_portions = models.SmallIntegerField(default=1)
    portion_size = models.PositiveIntegerField(default=0)
    portion_unit =  models.CharField(
        max_length = 5, 
        choices = PORTION_UNIT_CHOICES, 
        default = units.NA
    )
    portion_detail = models.CharField(
        default = '-',
        max_length = 100
    )    

    favourite = models.BooleanField(default = False)
    draft = models.BooleanField(default = False)

    detail = models.TextField(default = "-")
    steps = models.TextField(default = "-")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = RecipeManager()

    def save(self, *args, **kwargs):
        if not self.portion_unit in Recipe.PORTION_UNITS:
            raise ValueError('The unit {} is not allowed'.format(self.portion_unit)) 
        else:
            super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "recipes"
        verbose_name = "recipe"
        verbose_name_plural = "recipes"
        ordering = ["category"]
        get_latest_by = "updated"
        unique_together = ("title", "category",)
        index_together = ["title", "category"]    


class IngredientInRecipe(models.Model):
    
    INGREDIENT_MEASURE_UNITS = (
        units.GR,
        units.ML,
        units.UN,
        units.PINCH,
        units.DASH,
        units.CN,
    )
    
    UNIT_CHOICES = (
        (INGREDIENT_MEASURE_UNITS[0], 'gr'),
        (INGREDIENT_MEASURE_UNITS[1], 'ml'),
        (INGREDIENT_MEASURE_UNITS[2], 'un'),
        (INGREDIENT_MEASURE_UNITS[3], 'pinch'),
        (INGREDIENT_MEASURE_UNITS[4], 'dash'),
        (INGREDIENT_MEASURE_UNITS[5], 'c/n'),
    )    
    
    recipe = models.ForeignKey(
        Recipe,
        related_name = "appears",
        on_delete = models.CASCADE
    )

    ingredient = models.ForeignKey(
        Ingredient,
        related_name = "recipes",
        on_delete = models.PROTECT
    )
        
    amount = models.DecimalField(
        max_digits = 6, 
        decimal_places = 2, 
        default = 0
    )
    
    unit = models.CharField(
        max_length = 5, 
        choices = UNIT_CHOICES, 
        default = units.CN
    )
    
    optional = models.BooleanField(default = False)
    relevant = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        if not self.unit in IngredientInRecipe.INGREDIENT_MEASURE_UNITS:
            raise ValueError('The unit {} is not allowed'.format(self.unit)) 
        else:
            super(IngredientInRecipe, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.recipe.title

    class Meta:
        db_table = "recipes_ingredients_in_recipes"
        verbose_name = "Ingredient in recipes"
        verbose_name_plural = "Ingredients in recipes"
        ordering = ["recipe"]
        unique_together = ("recipe", "ingredient",)
        index_together = ["recipe", "ingredient"]
