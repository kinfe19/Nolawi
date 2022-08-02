from django.urls import path
<<<<<<< HEAD
from .views import *

app_name = 'crudapp'
urlpatterns = [
    path("", hello, name="hello"),
]

=======
from . import views


urlpatterns = [
    path('',views.index),
    
]
>>>>>>> 9a77cd3ddc9b0a96b9bd2dce892d70a267cf4cdb
