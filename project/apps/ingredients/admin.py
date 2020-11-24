from django.contrib import admin
from .models import IngredientCategory, Ingredient


class IngredientAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Main', {
            'fields': (
                'title',
                'category',
                'detail',
            )
        }),
    )

    list_display = ("title","category",)
    list_filter = ("category",)
    list_select_related = ("category",)


admin.site.register(IngredientCategory)
admin.site.register(Ingredient, IngredientAdmin)
