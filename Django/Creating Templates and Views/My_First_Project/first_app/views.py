from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')


def album_list(request):
    return render(request,'first_app/album_list.html')

def musician_form(request):
    return render(request,'first_app/musician_form.html')

def album_form(request):
    return render(request,'first_app/album_form.html')
