from rest_framework import routers
from .api import ProjetViewSet

router = routers.DefaultRouter()

router.register("api/projects", ProjetViewSet, "projects" )

urlpatterns = router.urls
