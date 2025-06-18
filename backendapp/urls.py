# from django.urls import path,include 
# from rest_framework.routers import DefaultRouter 
# from.import views
from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path


router = DefaultRouter()
router.register(r'role', views.RoleViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'specialization', views.SpecializationViewSet)
router.register(r'doctor', views.DoctorViewSet)
urlpatterns = router.urls