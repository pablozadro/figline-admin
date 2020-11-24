from django_filters import rest_framework as filters
from .models import Ingredient


class IngredientFilter(filters.FilterSet):

    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ingredient
        fields = [ 'title', 'category']
