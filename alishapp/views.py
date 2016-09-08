from django.shortcuts import render
from django.http import Http404
from .models import Research




# Create your views here.

def index(request) :
    All_Research=Research.objects.all()
    context={'All_Research':All_Research}
    return render(request,'alishapp/indexnew.html',context)

def ResearchDetails(request,Research_ID) :
    try :
        research=Research.objects.get(pk=Research_ID)
    except Research.DoesNotExist :
        raise Http404("Content does not exist")
    return render(request,'indexnew.html',{'research':research})

    

