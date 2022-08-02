from django.shortcuts import render


<<<<<<< HEAD
# Create your views here.

def hello(request):
    return render(request, 'crudapp/hello.html', {'name': 'World'})
=======
def index(request):
	return render(request, 'index.html')
>>>>>>> 9a77cd3ddc9b0a96b9bd2dce892d70a267cf4cdb
