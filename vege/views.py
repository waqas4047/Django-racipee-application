from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
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

        return redirect("display")

    return render(request, "recipe.html")


def display(request):
    queryset = Recipe.objects.all()
    if request.GET.get("Search"):

        queryset = queryset.filter(recipe_name__icontains=request.GET.get("Search"))

    context = {"recipes": queryset}
    return render(request, "display.html", context)


def delete_recipe(request, id):

    queryset = Recipe.objects.get(id=id)
    queryset.delete()

    return redirect("display")


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_title = data.get("recipe_name")
        recipe_description = data.get("recipe_discription")
        recie_img = request.FILES.get("recipe_img")

        queryset.recipe_name = recipe_title
        queryset.recipe_discription = recipe_description

        if recie_img:
            queryset.recipe_img = recie_img

        queryset.save()

        return redirect(reverse("display"))

    context = {"recipe": queryset}
    return render(request, "update_recipe.html", context)
