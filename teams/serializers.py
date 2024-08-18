from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'project', 'user', 'role', 'added_at']
        read_only_fields = ['added_at']