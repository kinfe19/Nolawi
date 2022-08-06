from django.urls import path
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path("/home", index, name="op"),
    path("",list,name=list),

    path("high",retrive,name="high")
]

