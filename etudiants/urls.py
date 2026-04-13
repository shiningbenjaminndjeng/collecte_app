from rest_framework.routers import DefaultRouter
from .views import EtudiantViewSet

router = DefaultRouter()
router.register('etudiants', EtudiantViewSet)

urlpatterns = router.urls