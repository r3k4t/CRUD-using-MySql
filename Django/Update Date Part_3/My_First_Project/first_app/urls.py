from django.urls import include,path
# form first_app import views or
from . import views

app_name = "first_app"

urlpatterns=[
   path('',views.index,name='index'),
   path('add_album/',views.album_form,name='album_form'),
   path('add_musician/',views.musician_form,name='musician_form'),
   path('album_list/<int:artist_id>/',views.album_list,name='album_list'),
   path('edit_artist/<int:artist_id>/',views.edit_artist,name='edit_artist'),
   path('edit_album/<int:album_id>/',views.edit_album,name='edit_album')

]
