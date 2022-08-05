from django.urls import include, path
from rest_framework.routers import DefaultRouter;

from .views import UploadViewSet;

# object = ClassName();
# object.method();
# object.property
router = DefaultRouter();
router.register(r'upload', UploadViewSet, basename="upload");
urlpatterns = [
     path(r"", include(router.urls)),
]
