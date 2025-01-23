from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_discription = models.TextField()
    # upload to recipe it will create a folder when we send file from  form to backend it will create recipe
    # folder and will save that file in recipe folder
    recipe_img = models.ImageField(upload_to="recipe")
