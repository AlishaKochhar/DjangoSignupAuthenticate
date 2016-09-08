from django.shortcuts import render,render_to_response,RequestContext
from .forms import UserRegisForm
from django.core.context_processors import csrf
#from django.http import HttpResponse

# Create your views here.

def signup(request) :
    #return HttpResponse("<h1>Hello</h1>")
    form=UserRegisForm(request.POST or None)
    if form.is_valid() :
        save_it=form.save(commit=False)
        save_it.save()
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

