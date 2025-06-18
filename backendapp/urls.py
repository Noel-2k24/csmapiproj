# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views
#---------------------------------------------------------------------------------------------------------------
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ConsultationBillingViewSet

# router = DefaultRouter()
# router.register(r'billing', ConsultationBillingViewSet, basename='consultationbilling')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
#---------------------------------------------------------------------------------------------------------------

# backendapp/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ConsultationBillingViewSet

# router = DefaultRouter()
# router.register(r'billing', ConsultationBillingViewSet, basename='consultationbilling')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
#--------------------------------------------------------------------------------------------------
# from django.urls import path
# from .views import (
#     create_consultation_billing,
#     update_consultation_billing,
#     get_consultation_billing_by_appointment,
#     list_consultation_bills_by_date_range
# )

# urlpatterns = [
#     path('billing/', create_consultation_billing, name='create-consultation-billing'),
#     path('billing/<int:billing_id>/', update_consultation_billing, name='update-consultation-billing'),
#     path('billing/appointment/<int:appointment_id>/', get_consultation_billing_by_appointment, name='get-billing-by-appointment'),
#     path('billing/history/', list_consultation_bills_by_date_range, name='billing-history'),
# ]

#-------------------------------------------------------------------------------------------------------------
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, AppointmentViewSet, ConsultationBillViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'bills', ConsultationBillViewSet)
#router.register(r'bills', ConsultationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#-----------------------------------------------------------------
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ConsultationBillViewSet

# router = DefaultRouter()
# router.register(r'bills', ConsultationBillViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
