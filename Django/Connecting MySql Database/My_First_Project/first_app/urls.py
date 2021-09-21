from django.urls import include,path
# form first_app import views or
from . import views

app_name = "first_app"

urlpatterns=[
   path('',views.index,name='index'),
   path('form/',views.form,name='form')
]
