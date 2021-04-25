from rest_framework import routers, urlpatterns
from .api import GuiasViewSet

router = routers.DefaultRouter()
router.register('api/guias', GuiasViewSet, 'guias')

urlpatterns = router.urls
