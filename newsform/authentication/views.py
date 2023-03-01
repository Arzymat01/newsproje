from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "authentication/login.html", {
                "error": "Ошибка!!!"
            })

    return render(request, "authentication/login.html")


def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "authentication/register.html",
                              {
                                  "error": "Имя ползователя используется!!!",
                                  "username": username,
                                  "email": email,
                                  "firstname": firstname,
                                  "lastname": lastname
                              })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "authentication/register.html",
                                  {
                                      "error": "Email адресс используется!!!",
                                      "username": username,
                                      "email": email,
                                      "firstname": firstname,
                                      "lastname": lastname
                                  })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname,
                                                    password=password)
                    user.save()
                    return redirect("login")

        else:
            return render(request, "authentication/register.html",
                          {
                              "error": "Пароль неправилный!!!",
                              "username": username,
                              "email": email,
                              "firstname": firstname,
                              "lastname": lastname

                          })
    return render(request, "authentication/register.html")


def dashboard(request):

    return render(request, 'authentication/dashboard.html',)
