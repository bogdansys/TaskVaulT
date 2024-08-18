from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class Team(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')
    role = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Member', 'Member')])
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {self.role}"