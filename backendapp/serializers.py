# from rest_framework import serializers
# from .models import *

# serializers.py

# from rest_framework import serializers
# from .models import ConsultationBilling

# class ConsultationBillingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConsultationBilling
#         fields = '__all__'

#     def validate(self, data):
#         base = data.get('BaseAmount', 0)
#         tax = data.get('Tax', 0)
#         discount = data.get('Discount', 0)
#         data['TotalAmount'] = base + tax - discount
#         return data

from rest_framework import serializers
from .models import Appointment, Doctor,ConsultationBill #, Consultation

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

# class ConsultationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Consultation
#         fields = '__all__'

class ConsultationBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationBill
        fields = '__all__'
