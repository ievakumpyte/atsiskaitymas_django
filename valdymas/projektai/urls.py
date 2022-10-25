from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjektasListView.as_view(), name='projects'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('register/', views.register, name='register'),
    path('myprojects/', views.UserProjectsListView.as_view(), name='my-projects'),
    # path('myprojects/', views.UsersProjects, name='my-projects'),

]