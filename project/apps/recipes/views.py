from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Recipe
from .filters import RecipeFilter
from .serializers import RecipeSerializer


class RecipesList(APIView):
    """
    List all recipes, or create a new recipe.
    """
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]
    filterset_class = RecipeFilter

    def get(self, request, format=None):
        recipes = Recipe.objects.list()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({
            'message': 'recipes fetched successfully',
            'payload': {
                'len': len(serializer.data),
                'recipes': serializer.data
            }
        })

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(APIView):
    """
    Retrieve, update or delete a recipe instance.
    """

    lookup_field = 'id'
    permission_classes = [ permissions.IsAuthenticated ]

    def get_object(self, id):
        try:
            return Recipe.objects.detail(id)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        recipe = self.get_object(id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        recipe = self.get_object(id)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        recipe = self.get_object(id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)