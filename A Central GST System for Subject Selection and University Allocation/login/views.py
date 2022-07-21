from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as user_login
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        registration = request.POST['registration']
        user = authenticate(username = username,password = registration)
        # logout(request)
        if user is not None:
            print('this ',registration)
            user_login(request, user)
            # logout(request)
            return redirect('/subjectselection/')

        # print(username,registration)
        else:
            return redirect('/registration/')

    return render(request, 'login/login.html')
def logoutuser(request):
    logout(request)
    return redirect('/registration/')
