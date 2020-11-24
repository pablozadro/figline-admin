from .models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only = True)

    class Meta:
        model = Recipe
        fields = [
          'id', 
          'title',
          'category',
          'category_title'
        ]