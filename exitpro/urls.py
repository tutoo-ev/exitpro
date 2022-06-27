from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="EV Exit Pro Project",
      default_version='v1',
      description="Program to handle employee relieval",
      terms_of_service="ev terms",
      contact=openapi.Contact(email="evcontact@ev.com"),
      license=openapi.License(name="EV License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    ## Token handling for Registered Users
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ## User related apis
    path('api/users/', include('apps.user.urls')),
    path('api/departments/', include('apps.departments.urls')),
    # path('openapi', get_schema_view(
    #     title="ExitPro Project",
    #     description="APIs for ExitPro Project",
    #     version="1.0.0"
    # ), name='openapi-schema'),
    # path('', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url': 'openapi-schema'}
    # ), name='swagger-ui'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
