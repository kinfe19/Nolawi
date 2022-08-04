from django.urls import path
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path("", index, name="index"),
    path("create/", list, name="create"),
]

