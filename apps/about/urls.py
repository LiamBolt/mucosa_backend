from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    TeamMemberListAPIView,
    ImpactMetricListAPIView,
    ContactSubmissionCreateAPIView
)

schema_view = get_schema_view(
    openapi.Info(
        title="About API",
        default_version='v1',
        description="Comprehensive API documentation for the About page endpoints. "
                    "This includes endpoints for team members, impact metrics, and secure contact submissions.",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # About API endpoints
    path('team/', TeamMemberListAPIView.as_view(), name='team-member-list'),
    path('impact/', ImpactMetricListAPIView.as_view(), name='impact-metric-list'),
    path('contact/', ContactSubmissionCreateAPIView.as_view(), name='contact-submission-create'),
    
    # Swagger UI documentation endpoint
    path('about/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc documentation endpoint for an alternative view
    path('about/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
