from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.login_page, name="login"),
    path("display/", views.display, name="display"),
    path("delete_recipe/<id>/", views.delete_recipe, name="delete_recipe"),
    path("update_recipe/<id>/", views.update_recipe, name="update_recipe"),
    path("recipe/", views.recipe, name="recipe"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register, name="register"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
