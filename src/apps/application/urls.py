from django.urls import path

from apps.application.views import DeleteTask, TablePage


app_name = 'application'

urlpatterns = [
    path('', TablePage.as_view(), name='main-page'),
    
    path('api/delete-task/<int:task_id>', DeleteTask.as_view(), name='delete-task')
]