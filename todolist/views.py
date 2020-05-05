from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import Task
from .forms import TaskForm


class IndexView(generic.ListView):
    # context_object_name = 'task_list'
    # template_name = 'totdolist/index.html'

    def get_queryset(self):
        return Task.objects.all()


class DetailView(generic.DetailView):
    model = Task


def create(request):
    form = TaskForm(request.POST)
    # breakpoint()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'todolist/create.html',{'form': form})
    form = TaskForm()
    return render(request,'todolist/create.html',{'form': form})


def edit(request, pk, template_name='todolist/edit.html'):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})


def delete(request, pk, template_name='todolist/confirm_delete.html'):
    task = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request, template_name, {'object':task})



def done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.task_done()
    task.save()
    return redirect('/')
