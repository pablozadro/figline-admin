from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.recipes.models import IngredientInRecipe
from .models import Ingredient
from .filters import IngredientFilter
from .serializers import IngredientSerializer


class IngredientList(generics.ListCreateAPIView):
    """
    List all ingredients, or create a new one.
    """
    queryset = Ingredient.objects.list()
    serializer_class = IngredientSerializer
    filterset_class = IngredientFilter
    permission_classes = [ permissions.IsAuthenticated ]


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or remove a ingredient.
    """
    queryset = Ingredient.objects.list()
    serializer_class = IngredientSerializer
    lookup_field = 'id'
    permission_classes = [ permissions.IsAuthenticated ]