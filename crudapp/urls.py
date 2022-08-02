from django.urls import path
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path("", hello, name="hello"),
]

