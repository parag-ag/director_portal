from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if request.user.is_active:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('dashboard'))

                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        else:
            return render(request, 'home/login.html', {})

def dashboard(request):
    if request.user.is_active:
        return render(request,'home/dashboard.html',
                              {'user_info':request.user,})
    else:
        return HttpResponseRedirect(reverse('user_login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
