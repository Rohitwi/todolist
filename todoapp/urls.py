from django.urls import path
from . import views

urlpatterns = [
    path('', views.showlist, name='showlist'),
    path('add/', views.add_task, name='add_task'),
    path('remove/<int:task_id>/', views.remove_task, name='remove_task'),
]
