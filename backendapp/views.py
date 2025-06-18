from django.shortcuts import render

from .serializers import AppointmentSerializer,DoctorSerializers,PatientSerializers
from rest_framework import viewsets
from .models import Doctor,Appointment,Patient
# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializers
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializers
    

    