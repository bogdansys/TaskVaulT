from django.urls import path
from .views import TeamListCreateView, TeamDetailView

urlpatterns = [
    path('projects/<int:project_id>/team/', TeamListCreateView.as_view(), name='team-list-create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
]