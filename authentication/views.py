from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def LoginPage(request):

    if request.user.is_authenticated :

        return redirect('home')

    context={
       "error" : ""
    }

    if request.method == 'POST':
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {
                "error" : "*Invalid Username or Password "
            }
            # return render(request, 'login.html', context)
    return render(request, 'login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect("/")

def SignupPage(request):

    context = {
        "error" : ""
    }

    if request.method == 'POST':

        user_check = User.objects.filter(username = request.POST['username'])
        if len(user_check) > 0 :
            context = {
                "error" : "*Username Already Exits!"
            }
            return render(request, 'signup.html', context)
        else:
            new_user = User(username = request.POST['username'], 
                            first_name = request.POST['firstname'], 
                            last_name = request.POST['lastname'], 
                            email = request.POST['email'], 
                            age = request.POST['age'],
                            role = request.POST['role'],)
            new_user.set_password(request.POST['password'])

            new_user.save()
            return redirect('login')
    return render(request, 'signup.html', context)


