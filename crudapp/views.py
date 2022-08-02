from django.shortcuts import render


def hello(request):
    return render(request, 'crudapp/hello.html', {'name': 'World'})


def index(request):
    return render(request, 'index.html')
