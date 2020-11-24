from decimal import *
from django.db import models

from apps.tools import units
from .managers import IngredientManager


class IngredientCategory(models.Model):

    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "ingredients_categories"
        verbose_name = "category"
        verbose_name_plural = "categories"


class Ingredient(models.Model):
    
    title = models.CharField(
        db_index = True, 
        max_length = 100
    )    
    
    category = models.ForeignKey(
        IngredientCategory,
        related_name = "ingredients",
        on_delete = models.PROTECT
    )    

    detail = models.TextField(default = "-")

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    objects = IngredientManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "ingredients"
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"
        ordering = ["title"]
        get_latest_by = "updated"
        unique_together = ("title", "category")
        index_together = ["title", "category"]  
