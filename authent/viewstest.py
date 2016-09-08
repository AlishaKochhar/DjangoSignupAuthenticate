from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from UserRegis.models import UserRegis

# Create your views here.

def login(request) :
    c={}
    c.update(csrf(request))
    return render_to_response('authent/login.html',c)

def auth_view(request) :
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    x=UserRegis.objects.all()
    n=len(x)
    username2=[]
    password2=[]
    flag=0
    for i in range(0,n) :
        username2.append(x[i].first_name)
        password2.append(x[i].password)
    
    for i in range(0,n) :
        print(username2[i])
        print(password2[i])
        if(username==username2[i] and password==password2[i]) :
            flag=1
            break

        if flag==1 :
            user=auth.authenticate(username=username2[i],password=password2[i])
            if user is not None :
                auth.login(request,user)
                return HttpResponseRedirect('loggedin')

            else :
                return HttpResponseRedirect('invalid')

def loggedin(request) :
    return render_to_response('authent/loggedin.html',{'full_name':request.user.first_name})

def invalid_login(request) :
    return render_to_response('authent/invalid_login.html')

def logout(request) :
    auth.logout(request)
    return render_to_response('authent/logout.html')
        
