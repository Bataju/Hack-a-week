from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def index(request):
    #return HttpResponse("THIS IS THE HOME PAGE")
    return render(request, "register\index.html")