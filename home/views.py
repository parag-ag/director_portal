from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_active:
        return render(request,'home/dashboard.html',{'user_info':request.user,})
    else:
        return render(request,'home/login.html',{})
