from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
     path(r"", include(("app_name.urls", "app_name"), namespace="api")),
]
