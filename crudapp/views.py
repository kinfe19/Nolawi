from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreationForm
<<<<<<< HEAD
var = "bek"
=======
bb = "opppps"
>>>>>>> fde2f8f7585b4630d9a9d2f9d291c56085060354
def list(request):
    task = Task.objects.all()
    return JsonResponse(task,safe=False)

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