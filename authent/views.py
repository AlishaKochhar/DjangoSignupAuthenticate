from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from UserRegis.models import UserRegis
from UserRegis.forms import UserRegisForm

# Create your views here.

def login(request) :
    c={}
    c.update(csrf(request))
    return render_to_response('authent/login.html',c)

def auth_view(request) :
    username3=request.POST.get('username')
    password3=request.POST.get('password')
    #user=auth.authenticate(username=username,password=password)

    x=UserRegis.objects.all()
    n=len(x)
    username2=[]
    password2=[]
    flag=0
    for i in range(0,n) :
        username2.append(x[i].username)
        password2.append(x[i].password)
    
    for i in range(0,n) :
        print(username2[i],"  ",username3)
        print(password2[i],"  ",password3)

        if(username3==username2[i] and password3==password2[i]) :
            #auth.login(request)
            return HttpResponseRedirect('loggedin')
        

        if(i==n-1) :
            return HttpResponseRedirect('invalid')
       
   #if user is not None :
    #    auth.login(request,user)
     #   return HttpResponseRedirect('loggedin')

    #else :
     #   return HttpResponseRedirect('invalid')'''

def loggedin(request) :
    return render_to_response('authent/loggedin.html',{'full_name':request.user.username})

def invalid_login(request) :
    return render_to_response('authent/invalid_login.html')

def logout(request) :
    auth.logout(request)
    return render_to_response('authent/logout.html')
        
