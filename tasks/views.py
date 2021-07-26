from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from tasks.models import Task
from tasks.forms import TaskForm
from .tasks import execute_task


class TaskListView(ListView):
    model = Task
    template_name = "list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "form.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "detail.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "form.html"


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self, *args, **kwargs):
        return reverse("task-list")

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


def execute_task_view(request, id):
    instance = get_object_or_404(Task, pk=id)
    instance.status = "em_espera"
    instance.save()
    
    execute_task.delay(id)

    return redirect(instance.get_absolute_url())


def get_task_info(request, id):
    instance = get_object_or_404(Task, pk=id)

    return JsonResponse({
        "status": instance.status,
        "label": instance.status_display,
        "espera": instance.tempo_espera
    })


    