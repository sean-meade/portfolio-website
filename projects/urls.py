from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects_tag/<int:tag_id>', views.projects_tag, name='projects_tag'),
]
