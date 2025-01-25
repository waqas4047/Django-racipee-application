from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from vege.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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


def login_page(request):
    if request.method == "POST":
        uname = request.POST.get("u_name")
        passwd = request.POST.get("paswd")

        if not User.objects.filter(username=uname).exists():
            messages.error(request, "invalid username")
            return redirect("/")

        user = authenticate(username=uname, password=passwd)

        if user is None:
            messages.error(request, "invalid credentials")
            return redirect("/")
        else:
            login(request, user)
            return redirect("/display")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/")


def register(request):

    if request.method == "POST":
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        uname = request.POST.get("username")
        passwd = request.POST.get("password")

        user = User.objects.filter(username=uname)
        if user.exists():
            messages.info(request, "This username already exist!")
            return redirect("/register")

        user = User.objects.create(first_name=f_name, last_name=l_name, username=uname)
        user.set_password(passwd)
        user.save()

        messages.info(request, "Account created succesfully!")
        return redirect("/register")

    return render(request, "register.html")
