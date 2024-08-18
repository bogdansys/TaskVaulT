# tasks/views.py
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from notifications.models import Notification
import logging

logger = logging.getLogger(__name__)

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        logger.info(f"Fetching tasks for user: {user.id}")
        return self.queryset.filter(project__created_by=user)

    def perform_create(self, serializer):
        try:
            task = serializer.save()
            logger.info(f"Task created successfully: {task.id}")
            # Create notification
            Notification.objects.create(
                user=task.assigned_to,
                type='Task Assigned',
                message=f"You have been assigned a new task: {task.title}"
            )
        except Exception as e:
            logger.error(f"Error creating task: {str(e)}", exc_info=True)
            raise

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        logger.info(f"Fetching task details for user: {user.id}")
        return self.queryset.filter(project__created_by=user)

    def perform_update(self, serializer):
        try:
            task = serializer.save()
            logger.info(f"Task updated successfully: {task.id}")
            # Create notification
            Notification.objects.create(
                user=task.assigned_to,
                type='Task Updated',
                message=f"Task '{task.title}' has been updated."
            )
        except Exception as e:
            logger.error(f"Error updating task: {str(e)}", exc_info=True)
            raise

    def perform_destroy(self, instance):
        try:
            task_id = instance.id
            instance.delete()
            logger.info(f"Task deleted successfully: {task_id}")
        except Exception as e:
            logger.error(f"Error deleting task: {str(e)}", exc_info=True)
            raise