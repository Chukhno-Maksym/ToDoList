from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm
from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/tasks_list.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:tasks_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:tasks_list")

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:tasks_list")


class TaskCompleteView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = True
        task.save()
        return redirect("todo:tasks_list")


class TaskUndoView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = False
        task.save()
        return redirect("todo:tasks_list")