from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.recipes.models import IngredientInRecipe
from .models import Ingredient
from .filters import IngredientFilter
from .serializers import IngredientSerializer



class IngredientsList(APIView):
    """
    List all ingredients, or create a new ingredient.
    """
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]
    filterset_class = IngredientFilter

    def get(self, request, format=None):
        ingredients = Ingredient.objects.list()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response({
            'message': 'ingredients fetched successfully',
            'payload': {
                'len': len(serializer.data),
                'ingredients': serializer.data
            }
        })

    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientDetail(APIView):
    """
    Retrieve, update or delete a ingredient instance.
    """

    lookup_field = 'id'
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]

    def get_object(self, id):
        try:
            return Ingredient.objects.detail(id)
        except Ingredient.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        ingredient = self.get_object(id)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        ingredient = self.get_object(id)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        ingredient = self.get_object(id)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)