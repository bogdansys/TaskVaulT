from django.urls import path, include
from .views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:project_id>/', include('tasks.urls')),  # Include task URLs
    path('', include('teams.urls')),  # Include team URLs
]