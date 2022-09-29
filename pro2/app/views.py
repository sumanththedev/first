from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def moon(request):
    return HttpResponse("<center><h1>hello world </h1></center>")