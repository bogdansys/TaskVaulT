from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
import logging

logger = logging.getLogger(__name__)

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        logger.info(f"Fetching projects for user: {user.id}")
        return self.queryset.filter(created_by=user)

    def perform_create(self, serializer):
        try:
            project = serializer.save(created_by=self.request.user)
            logger.info(f"Project created successfully: {project.id}")
        except Exception as e:
            logger.error(f"Error creating project: {str(e)}", exc_info=True)
            raise

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        logger.info(f"Fetching project details for user: {user.id}")
        return self.queryset.filter(created_by=user)

    def perform_update(self, serializer):
        try:
            project = serializer.save()
            logger.info(f"Project updated successfully: {project.id}")
        except Exception as e:
            logger.error(f"Error updating project: {str(e)}", exc_info=True)
            raise

    def perform_destroy(self, instance):
        try:
            project_id = instance.id
            instance.delete()
            logger.info(f"Project deleted successfully: {project_id}")
        except Exception as e:
            logger.error(f"Error deleting project: {str(e)}", exc_info=True)
            raise