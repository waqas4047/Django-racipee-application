from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.recipe, name="recipe"),
    path("display/", views.display, name="display"),
    path("delete_recipe/<id>/", views.delete_recipe, name="delete_recipe"),
    path("update_recipe/<id>/", views.update_recipe, name="update_recipe"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
