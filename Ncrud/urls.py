<<<<<<< HEAD

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


=======
from django.contrib import admin
from django.urls import path,include



>>>>>>> 9a77cd3ddc9b0a96b9bd2dce892d70a267cf4cdb
urlpatterns = [

    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('crudapp.urls'), name='crudapp'),
=======
    path('', include('crudapp.urls')),

>>>>>>> 9a77cd3ddc9b0a96b9bd2dce892d70a267cf4cdb
]
