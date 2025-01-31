from asyncio import tasks

from django.urls import path

from todo.views import (TaskListView,
                        TaskCreateView,
                        TaskUpdateView,
                        TaskDeleteView,
                        TaskCompleteView,
                        TaskUndoView,
                        TagListView,
                        TagCreateView,
                        TagUpdateView,
                        TagDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks_list"),
    path("create/", TaskCreateView.as_view(), name="task_form"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("complete/<int:pk>/", TaskCompleteView.as_view(), name="task_complete"),
    path("undo/<int:pk>", TaskUndoView.as_view(), name="task_undo"),
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_form"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "todo"