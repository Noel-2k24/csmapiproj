from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'consultation', views.CounsultationViewSet)
urlpatterns = router.urls