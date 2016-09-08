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
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect('loggedin')

    else :
        return HttpResponseRedirect('invalid')

def loggedin(request) :
    return render_to_response('authent/loggedin.html',{'full_name':request.user.username})

def invalid_login(request) :
    return render_to_response('authent/invalid_login.html')

def logout(request) :
    auth.logout(request)
    return render_to_response('authent/logout.html')
        
