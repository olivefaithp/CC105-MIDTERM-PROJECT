from django.urls import path
from .views import task_list, task_create, task_update, task_delete, mark_task_done

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:id>/edit/', task_update, name='task_update'),
    path('task/<int:id>/delete/', task_delete, name='task_delete'),
    path('task/<int:id>/done/', mark_task_done, name='task_done'),  # Add this line
]
