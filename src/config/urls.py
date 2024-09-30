from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Diary Project API",
        default_version="v1",
        description="This is Swagger Docs of Diary Project",
        contact=openapi.Contact(email="v4chelsea@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # Swagger UI:
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # apps
    path("api/v1/diary/", include("diary.urls.prod")),
    path("api/v1/image/", include("image.urls")),
    path("api/v1/tag/", include("tag.urls")),
    path("api/v1/oauth/", include("oauth.urls")),
    path("api/v1/user/", include("user.urls")),
    # dev
    path("api/v1/dev/diary/", include("diary.urls.dev")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
