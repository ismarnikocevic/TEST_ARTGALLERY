
from django.shortcuts import (get_object_or_404,render, HttpResponseRedirect)
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.shortcuts import render
from pprint import pprint
import inspect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



def index(request):
    return render(request, 'dom.html', locals())

def dom(request):
    return render(request, 'dom.html', locals())


def blog(request):
    return render(request, 'blog.html', locals())

def biography(request):
    return render(request, 'biography.html', locals())

def gallery(request):
    return render(request, 'gallery.html', locals())

def album(request):
    return render(request, 'album.html', locals())


def photo1(request):
    return render(request, 'photo1.html', locals())

def slika2(request):
    return render(request, 'slika2.html', locals())

def photo2(request):
    return render(request, 'photo2.html', locals())

def photo3(request):
    return render(request, 'photo3.html', locals())

def photo4(request):
    return render(request, 'photo4.html', locals())

def photo5(request):
    return render(request, 'photo5.html', locals())

def photo6(request):
    return render(request, 'photo6.html', locals())

def photo7(request):
    return render(request, 'photo7.html', locals())

def photo8(request):
    return render(request, 'photo8.html', locals())

def photo9(request):
    return render(request, 'photo9.html', locals())

def photo10(request):
    return render(request, 'photo10.html', locals())

def photo11(request):
    return render(request, 'photo11.html', locals())

def photo12(request):
    return render(request, 'photo12.html', locals())


def photo13(request):
    return render(request, 'photo13.html', locals())

def photo14(request):
    return render(request, 'photo14.html', locals())

def photo15(request):
    return render(request, 'photo15.html', locals())

def photo16(request):
    return render(request, 'photo16.html', locals())

def photo17(request):
    return render(request, 'photo17.html', locals())

def photo18(request):
    return render(request, 'photo18.html', locals())

def photo19(request):
    return render(request, 'photo19.html', locals())



def primjer(request):
    return render(request, 'primjer.html', locals())

def index(request):
    return render(request, 'index.html', locals())


