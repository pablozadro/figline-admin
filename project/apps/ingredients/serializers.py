from .models import Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only = True)

    class Meta:
        model = Ingredient
        fields = [
          'id', 
          'title',
          'category',
          'category_title'
        ]