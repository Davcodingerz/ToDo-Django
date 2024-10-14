from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.utils import timezone
from datetime import timedelta
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    current_time = timezone.now()
    one_day_from_now = current_time + timedelta(days=1)
    return render(request, "index.html", {"tasks":tasks, "current_time":current_time, "one_day_from_now":one_day_from_now})

def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/todolist/task")
    else :
        form = TaskForm()
    return render(request, "create.html", {"form":form})

def update(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/todolist/task")
    else:
        form = TaskForm(instance=task)
    return render(request, "update.html", {"form":form})
def delete(request,pk):
    task = get_object_or_404(Task, pk =pk)
    if request.method == "POST":
        task.delete()
        return redirect("/todolist/task")
    return render(request, "delete.html", {"task":task})
    