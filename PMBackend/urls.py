from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger and ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="PMBackend API",
        default_version='v1',
        description="API documentation for the PMBackend project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('projects.urls')),  # Include project URLs
    path('api/', include('tasks.urls')),  # Include task URLs
    path('api/', include('teams.urls')),  # Include team URLs
    path('api/', include('logentries.urls')),  # Include log URLs
    path('api/', include('notifications.urls')),  # Include notification URLs

    # Swagger and ReDoc paths
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
