from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from .serializers import RegisterSerializer, UserSerializer, UserProfileSerializer, UserRoleSerializer
from .models import User
import logging

# Set up logging
logger = logging.getLogger(__name__)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            logger.info(f"User registered: {user.username}")
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]
            })
        except Exception as e:
            logger.error(f"Error during registration: {str(e)}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        from rest_framework import serializers
        from django.contrib.auth import authenticate

        # Define the serializer here since it was missing
        class AuthTokenSerializer(serializers.Serializer):
            username = serializers.CharField()
            password = serializers.CharField(
                style={'input_type': 'password'}, trim_whitespace=False)

            def validate(self, attrs):
                username = attrs.get('username')
                password = attrs.get('password')

                if username and password:
                    user = authenticate(request=self.context.get('request'),
                                        username=username, password=password)
                    if not user:
                        raise serializers.ValidationError('Unable to log in with provided credentials.', code='authorization')
                else:
                    raise serializers.ValidationError('Must include "username" and "password".', code='authorization')

                attrs['user'] = user
                return attrs

        serializer = AuthTokenSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            logger.info(f"User logged in: {user.username}")
            return super(LoginView, self).post(request, format=None)
        except Exception as e:
            logger.error(f"Error during login: {str(e)}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        logger.info(f"Retrieving profile for user: {user.username}")
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        logger.info(f"Updating profile for user: {user.username}")
        response = super().update(request, *args, **kwargs)
        logger.info(f"Profile updated for user: {user.username}")
        return response

class UserRoleView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        user = super().get_object()
        logger.info(f"Retrieving role for user: {user.username}")
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        logger.info(f"Updating role for user: {user.username}")
        response = super().update(request, *args, **kwargs)
        logger.info(f"Role updated for user: {user.username}")
        return response
