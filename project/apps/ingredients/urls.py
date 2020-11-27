from django.urls import path
from . import views

app_name = 'ingredients'

urlpatterns = [
    path('', views.IngredientsList.as_view(), name='list'),
    path('<int:id>', views.IngredientDetail.as_view(), name='detail')
]
