from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Recipe
from .filters import RecipeFilter
from .serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List all recipes, or create a new one.
    """
    queryset = Recipe.objects.list()
    serializer_class = RecipeSerializer
    filterset_class = RecipeFilter
    permission_classes = [ permissions.IsAuthenticated ]


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or remove a recipe.
    """
    queryset = Recipe.objects.list()
    serializer_class = RecipeSerializer
    lookup_field = 'id'
    permission_classes = [ permissions.IsAuthenticated ]