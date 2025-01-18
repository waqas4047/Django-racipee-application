from django.shortcuts import render
from django.http import HttpResponse
from vege.models import Recipe

# Create your views here.


def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_title = data.get("recipe_name")
        recipe_description = data.get("recipe_discription")
        recie_img = request.FILES.get("recipe_img")

        Recipe.objects.create(
            recipe_name=recipe_title,
            recipe_discription=recipe_description,
            recipe_img=recie_img,
        )

        return HttpResponse("your data was successfully stored")

    return render(request, "recipe.html")
