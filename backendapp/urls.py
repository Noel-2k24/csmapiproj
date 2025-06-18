# from rest_framework.routers import DefaultRouter
# from . import views
# from django.urls import path



# router = DefaultRouter()
# router.register(r'patients', views.PatientViewSet)
# router.register(r'appoinment', views.AppointmentViewSet)
# router.register(r'doctor', views.DoctorViewSet)


# urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'appointment', views.AppointmentViewSet)
router.register(r'doctor', views.DoctorViewSet)

urlpatterns = router.urls
