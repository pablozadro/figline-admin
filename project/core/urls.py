from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.landing.urls')),
    path('api/v1/ingredients/', include('apps.ingredients.urls')),
    path('api/v1/recipes/', include('apps.recipes.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns