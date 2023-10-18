from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, About


@login_required 
def index(request):
    return render(request, "maths/index.html") 

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            # **NEW:** Pass the user object to the login() function
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "maths/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "maths/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        school = request.POST["school"]
        country = request.POST["country"]
        phone = request.POST["phone"]
        if password != confirmation:
            return render(request, "maths/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "maths/register.html", {
                "message": "User with that username or email already exists."
            })

        if request.user.is_authenticated:
            try:
                about = About.objects.create(Author=user, school=school, country=country, phone_number=phone)
                about.save()
            except IntegrityError:
                return render(request, "maths/register.html", {
                    "message": "User with that school and country already exists."
                })

        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "maths/register.html")

        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def home(request):
    return render(request, "maths/home.html") 

    