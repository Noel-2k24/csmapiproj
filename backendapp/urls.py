from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path

router=DefaultRouter()
router.register(r'membership',views.MembershipViewSet)
router.register(r'patient',views.PatientViewSet)
urlpatterns = router.urls