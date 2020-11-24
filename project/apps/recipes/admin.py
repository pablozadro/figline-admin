from django.contrib import admin
from .models import RecipeCategory, Recipe, IngredientInRecipe


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': (
                'title',
                'category',
                'favourite',
                'draft',
            )
        }),
        ('Cooking', {
            'fields': (
                'portion_portions',
                'portion_size',
                'portion_unit',
                'portion_detail',
                'detail',
                'steps',
            ),
        }),
    )
    list_display = ("title","category")
    list_filter = ("category",)
    list_select_related = ("category",)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': (
                'recipe',
                'ingredient',
                'optional',
                'relevant',
                'amount',
                'unit',
            )
        }),
    )
    list_display = ("recipe", "ingredient", "amount", "unit", "relevant",)
    list_filter = ("recipe",)
    list_select_related = ("recipe", "ingredient",)

admin.site.register(RecipeCategory)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
