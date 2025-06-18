from rest_framework import serializers
from .models import Doctor,Appointment,Patient




class PatientSerializers(serializers.ModelSerializer):
   class Meta:
       model= Patient
       fields = '__all__'
       
class AppointmentSerializer(serializers.ModelSerializer):
   class Meta:
       model= Appointment
       fields = '__all__'
       
class DoctorSerializers(serializers.ModelSerializer):
   class Meta:
       model= Doctor
       fields = '__all__'
       
