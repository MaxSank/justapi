from rest_framework import routers
from .api import RecordViewSet


router = routers.DefaultRouter()
router.register('api/record', RecordViewSet, 'record')

urlpatterns = router.urls
