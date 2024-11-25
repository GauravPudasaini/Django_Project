from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('index')  # Redirect to the index page
        else:
            return HttpResponse("Invalid username or password!")

    return render(request, 'login.html')  # Render login page if GET request

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return HttpResponse("Passwords do not match!")
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        return redirect('login')  # Redirect to login page after signup
    return render(request, 'signup.html')  # Render signup page if GET request


@login_required(login_url='login')  # Ensure the user is logged in to access the index page
def index_view(request):
    superusers = User.objects.filter(is_superuser=True)
    users = [
        {
            'username': user.username,
            'email': user.email,
            'role': 'Admin' if user.is_superuser else 'User',
        }
        for user in User.objects.all()
    ]

    superuser_username = superusers[0].username if superusers.exists() else "No Superadmin Found"

    context = {
        'superuser_username': superuser_username,
        'users': users,
    }
    return render(request, 'index.html', context)

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page
