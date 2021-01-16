from django.shortcuts import render,get_object_or_404,redirect
from django.http import  HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login,logout

from .models import User

# Create your views here.
def _index(request):
    latest_created_user_list = User.objects.order_by('-pub_date')[:5]
    print(latest_created_user_list)
    output = ', '.join([user.username+", "+user.pub_date for user in latest_created_user_list])
    template = loader.get_template('user/index.html')
    context = {
        'latest_created_user_list':latest_created_user_list
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'user/index.html', context)

def _detail(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    return render(request, 'user/detail.html',{'user':user})

def _signup(request):
    if request.method == 'POST':
        #print(requrest.POST)
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.firstname = firstname
        user.lastname = lastname
        user.save()
        return redirect("/auth")
    return render(request,"user/signup.html")

def _login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            print("authentication success")
            login(request,user)
        else:
            print('authentication failed')
    return render(request, 'user/login.html')

def _logout(request):
    logout(request)
    return redirect("/auth/login")