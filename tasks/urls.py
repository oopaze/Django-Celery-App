from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.TaskCreateView.as_view(), name="task-create"),
    path("detail/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("", views.TaskListView.as_view(), name="task-list"),
    path("execute/<int:id>/", views.execute_task_view, name="task-execute"),
    path("get_info/<int:id>/", views.get_task_info, name="task-info")
]
