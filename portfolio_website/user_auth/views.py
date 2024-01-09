from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "user_auth/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists.")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Account with email already exists.")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
    
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric.")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been created.")

        return redirect('login')
    return render(request, 'user_auth/signup.html')

def log_in(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "user_auth/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request, "user_auth/login.html")

def log_out(request):
    logout(request)
    messages.success(request, "Logged Out Succesfully!")
    return redirect("home")