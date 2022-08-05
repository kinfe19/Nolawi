from django.urls import path
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path("", index, name="index-changed-by-es"),
    path("",list,name=list),
    path("create/",create,name=create),
]

