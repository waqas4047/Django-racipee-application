from django.db import models

# Create your models here.


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_discription = models.TextField()
    # upload to recipe it will create a folder when we send file from  form to backend it will create recipe
    # folder and will save that file in recipe folder
    recipe_img = models.ImageField(upload_to="recipe")
