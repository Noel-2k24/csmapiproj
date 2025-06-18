# # core/urls.py

# from django.urls import path, include
# from .views import StaffLoginView

# urlpatterns = [
#     path('login/', StaffLoginView.as_view(), name='staff-login'),
#     # ... your other ViewSets registered with router
# ]

# from django.urls import path
# from .views import LoginView

# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login'),
# ]

# urls.py
# from django.urls import path
# from .views import StaffListView, PatientListView, AppointmentListView, CreateStaffView, UpdateConsultationStatus

# urlpatterns = [
#     path('staff/', StaffListView.as_view(), name='staff-list'),
#     path('staff/create/', CreateStaffView.as_view(), name='create-staff'),
#     path('patients/', PatientListView.as_view(), name='patient-list'),
#     path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
#     path('consultation/<int:pk>/update/', UpdateConsultationStatus.as_view(), name='update-consultation'),
# ]

from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]

