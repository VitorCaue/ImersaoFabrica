from django.shortcuts import render
from django.http import HttpResponse
from .form import Compraform, Compraform1, Compraform2, Compraform3
import datetime

from atv.models import Compra, Compra1, Compra2, Compra3


def home(request):
    now = datetime.datetime.now()
      
    return render(request, 'atv/home.html')

def loja(request):
    data ={}
    
    data['s'] = Compra.objects.all()
    data['i'] = Compra1.objects.all()
    data['c'] = Compra2.objects.all()
    data['t'] = Compra3.objects.all()

    return render(request, 'atv/loja.html', data)

def nova_compra(request):
    data = {}
    form = Compraform(request.POST or None)

    if form.is_valid():
        form.save()
        return loja(request)

    data['form'] = form
    return render(request, 'atv/op1.html', data)

def nova_compra1(request):
    data = {}
    form = Compraform1(request.POST or None)

    if form.is_valid():
        form.save()
        return loja(request)

    data['form'] = form
    return render(request, 'atv/op2.html', data)

def nova_compra2(request):
    data = {}
    form = Compraform2(request.POST or None)

    if form.is_valid():
        form.save()
        return loja(request)

    data['form'] = form
    return render(request, 'atv/op3.html', data)

def nova_compra3(request):
    data = {}
    form = Compraform3(request.POST or None)

    if form.is_valid():
        form.save()
        return loja(request)

    data['form'] = form
    return render(request, 'atv/op4.html', data)