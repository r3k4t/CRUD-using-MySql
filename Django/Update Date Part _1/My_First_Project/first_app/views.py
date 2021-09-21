from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms
from django.db.models import Avg

# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title':'Home Page','musician_list':musician_list}
    return render(request,'first_app/index.html',context=diction)


def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)


    diction = {'title':'Add Musician','musician_form':form}
    return render(request,'first_app/musician_form.html',context=diction)


def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)


    diction = {'title':'Add Album' ,'album_form':form}
    return render(request,'first_app/album_form.html',context=diction)


def album_list(request,artist_id):
    #when we use primary key.In this time,we also call get query
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist = artist_id).order_by('name','release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction = {'title':'List of Albums','artist_info':artist_info ,'album_list':album_list,'artist_rating':artist_rating}

    return render(request,'first_app/album_list.html',context=diction)



def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance = artist_info)
    diction = {'edit_form':form }
    return render(request,'first_app/edit_artist.html',context=diction)
