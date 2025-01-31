from asyncio import tasks

from django.urls import path

from todo.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        TaskCompleteView,
                        TaskUndoView)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks_list"),
    path("create/", TaskCreateView.as_view(), name="task_form"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("complete/<int:pk>/", TaskCompleteView.as_view(), name="task_complete"),
    path("undo/<int:pk>", TaskUndoView.as_view(), name="task_undo"),
]

app_name = "todo"