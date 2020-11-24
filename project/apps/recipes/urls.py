from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeList.as_view(), name='list'),
    path('<int:id>', views.RecipeDetail.as_view(), name='detail')
]
