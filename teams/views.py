from rest_framework import generics, permissions
from .models import Team
from .serializers import TeamSerializer
from projects.models import Project
import logging

logger = logging.getLogger(__name__)

class TeamListCreateView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        logger.info(f"Fetching team members for project: {project_id}")
        return Team.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(id=project_id)
        user = self.request.user
        if project.created_by != user:
            logger.error(f"User {user.username} is not authorized to add members to project {project_id}")
            raise PermissionDenied("You are not authorized to add members to this project.")
        serializer.save()
        logger.info(f"Team member added to project {project_id}")

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        team = self.get_object()
        user = self.request.user
        if team.project.created_by != user:
            logger.error(f"User {user.username} is not authorized to update team member {team.id}")
            raise PermissionDenied("You are not authorized to update this team member.")
        serializer.save()
        logger.info(f"Team member {team.id} updated")

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.project.created_by != user:
            logger.error(f"User {user.username} is not authorized to remove team member {instance.id}")
            raise PermissionDenied("You are not authorized to remove this team member.")
        instance.delete()
        logger.info(f"Team member {instance.id} removed")