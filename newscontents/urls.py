from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NewsContentViewSet

router = SimpleRouter()
router.register('news-content', NewsContentViewSet)
urlpatterns = router.urls