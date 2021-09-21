from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms

# Create your views here.

def index(request):
    #SELECT * FROM Musician ORDER BY first_name

    diction = {'sample_text':Album.objects.get(pk=2)}
    return render(request,'first_app/index.html',context=diction)


def form(request):
    new_form = forms.MusicianForm()

    if request.method == "POST":
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
             new_form.save(commit = True)
             return index(request)

    diction = {'test_form':new_form,'heading_1':'Add New Musician'}
    return render(request,'first_app/form.html',context=diction)
