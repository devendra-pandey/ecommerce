from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from order.models import Order

# Create your views here.

def signup(request):
    if request.method =="POST":
        ##to create the user ##
        if request.POST['password'] == request.POST['conf_pass']:
            ##both the pass match
            ##now check the user exists
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request, 'user/signup.html',{'error':"Username Alraedy has been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(first_name=request.POST['name'],username=request.POST['uname'],email=request.POST['email_ad'] ,password=request.POST['password'])
                ##this user can login afetr signup
                auth.login(request, user)
                return redirect("/")
        else:
            return render(request, 'user/signup.html',{'error':"Password Dont match"})         
    else:
        return render(request, 'user/signup.html')

def login(request):
    if request.method =="POST":
        ##che  if the user exist withthe pass
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request, 'user/login.html', {'error':"Invalid Login Credentials"})
    else:
        return render(request, 'user/login.html')
    
def user_dashboard(request):
    user_id = request.user.id
    order = Order.objects.filter(user = user_id).order_by("-id")
    return render(request, 'user/customer_dashboard.html',{'order':order})

def user_info(request):
    return render(request, 'user/customer_info.html')

def message(request):
    return render(request, 'user/message.html')

def message_comp(request):
    return render(request, 'user/message-compose.html') 


def recover_pass(request):
    return render(request, 'user/recover-pass.html')
     
def logout(request):
    auth.logout(request)
    return redirect('login')