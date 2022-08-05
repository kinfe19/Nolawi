from django.urls import path
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path("/home", index, name="op"),
    path("",list,name=list),
    path("l/" ,Nolawi ,name ="io"),
    path("l/" ,Nolawi ,name ="io"),
    path("op/",detail ,name="pop")



]

