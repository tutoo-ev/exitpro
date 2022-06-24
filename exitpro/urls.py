from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view




urlpatterns = [
    path('admin/', admin.site.urls),
    ## Token handling for Registered Users
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ## User related apis
    path('api/users/', include('apps.user.urls')),
    path('api/departments/', include('apps.departments.urls')),
    path('openapi', get_schema_view(
        title="ExitPro Project",
        description="APIs for ExitPro Project",
        version="1.0.0"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),



]
