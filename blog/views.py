from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 


def home(request): 
    date = datetime.now().date()   
    context = {'date': date}
    response = render(request, 'index.html', context)
    
    return HttpResponse(response) 

def root(request): 
    return HttpResponseRedirect('home') 
