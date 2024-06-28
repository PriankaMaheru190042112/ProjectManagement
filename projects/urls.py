from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:project_pk>/task/new/', views.task_create, name='task_create'),
    path('project/<int:project_pk>/task/<int:pk>/edit/', views.task_update, name='task_update'),
]
