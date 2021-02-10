from rest_framework.routers import DefaultRouter
from app import views
router = DefaultRouter()

router.register('Activity_Period', views.Activity_PeriodViewSet,basename='Activity_Period')
urlpatterns = router.urls