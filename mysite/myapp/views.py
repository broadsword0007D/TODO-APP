from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm
# Create your views here.


def index(request):
    task_list=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')

        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/index')
    return  render(request,r'C:\Users\rajha\OneDrive\Desktop\github.com\broadsword0007D\TODO-APP\mysite\myapp\templates\myapp\index.html',{'task_list':task_list})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/index')

    return render(request,'myapp/delete.html',{'task':task})


def update(request,taskid):
    task=Task.objects.get(id=taskid)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/index')
    
    return render(request, 'myapp/edit.html', {'form': form, "task": task})


def homepage(request):
    return render(request,r'C:\Users\rajha\OneDrive\Desktop\github.com\broadsword0007D\TODO-APP\mysite\myapp\templates\myapp\homepage.html')