from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


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


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags_list")