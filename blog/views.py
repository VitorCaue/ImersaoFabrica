from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chiclete(Request):
    
    return render(Request, template_name='blog/home.html')

def jujuba(Request):
    html = "<html><body><h1> Dê! </h1></body></html>"
    return HttpResponse(html)