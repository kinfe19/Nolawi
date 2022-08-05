from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreationForm
var =" mar mar"

variable = "1234"
def mare2(): 
    pass
def name():
    pass
def hello_page(request):
    return render(request, 'crudapp/hello.html', {'name': 'World'})
def list(request):
    task = Task.objects.all()
    return render(request, 'list.html',task)

def index(request):
    form = None
    if request.method == "POST":
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context ={"form":form}
    return render(request, 'crudapp/hello.html',context)
def update(request,pk):
    active = Task.objects.get(id=pk)
    form = TaskCreationForm(request.POST,instance=active)
    if form.is_valid():
               form.save()
               return redirect("/")
    context ={"form":form}
    return render(request, 'update.html',context)
def delete(request,pk):
    active = Task.objects.get(id=pk)
    if request.method =="POST":
        active.delete()
        return redirect("/")

    context ={"active":active}
    return redirect (request ,'delete.html',context)
def retrive(requets):
    task = Task.objects.all()
    return redirect (request, 'list.html',task)

def detail(request ,pk):
    active_detail = Task.objects.get(id=pk)

def Nolawi(request):
    pass