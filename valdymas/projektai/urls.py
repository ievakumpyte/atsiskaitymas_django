from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>', views.project, name='project'),
    path('register/', views.register, name='register'),
]