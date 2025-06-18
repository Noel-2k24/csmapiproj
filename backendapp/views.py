# from django.shortcuts import render
# from rest_framework import viewsets,permissions,filters
# from .models import *
# from .serializers import BillingSerializer
# from .permissions import IsReceptionist

# # Create your views here.

# class BillingViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.filter(IsActive=True)
#     serializer_class = BillingSerializer  # Assume separate serializer if needed
#     permission_classes = [permissions.IsAuthenticated, IsReceptionist]

#----------------------------------------------------------------------------------------------------------------
# views.py

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import ConsultationBilling, Appointment
# from .serializers import ConsultationBillingSerializer

# @api_view(['POST'])
# def create_consultation_billing(request):
#     appointment_id = request.data.get('AppointmentId')

#     # Check if billing already exists
#     if ConsultationBilling.objects.filter(AppointmentId_id=appointment_id).exists():
#         return Response({"error": "Bill already exists for this appointment"}, status=400)

#     # Check if appointment exists and is completed
#     try:
#         appointment = Appointment.objects.get(AppointmentId=appointment_id)
#         if appointment.ConsultationStatus.lower() != "completed":
#             return Response({"error": "Consultation not completed"}, status=400)
#     except Appointment.DoesNotExist:
#         return Response({"error": "Appointment not found"}, status=404)

#     serializer = ConsultationBillingSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


# @api_view(['PUT'])
# def update_consultation_billing(request, billing_id):
#     try:
#         billing = ConsultationBilling.objects.get(BillingId=billing_id)
#     except ConsultationBilling.DoesNotExist:
#         return Response({"error": "Billing not found"}, status=404)

#     serializer = ConsultationBillingSerializer(billing, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)


# @api_view(['GET'])
# def get_consultation_billing_by_appointment(request, appointment_id):
#     try:
#         billing = ConsultationBilling.objects.get(AppointmentId=appointment_id)
#         serializer = ConsultationBillingSerializer(billing)
#         return Response(serializer.data)
#     except ConsultationBilling.DoesNotExist:
#         return Response({"error": "No billing found for this appointment"}, status=404)


# @api_view(['GET'])
# def list_consultation_bills_by_date_range(request):
#     start = request.GET.get('startDate')
#     end = request.GET.get('endDate')

#     if start and end:
#         bills = ConsultationBilling.objects.filter(CreatedDate__range=[start, end])
#     else:
#         bills = ConsultationBilling.objects.all()

#     serializer = ConsultationBillingSerializer(bills, many=True)
#     return Response(serializer.data)
  
from rest_framework import viewsets
from .models import Appointment,Doctor,ConsultationBill #Consultation
from .serializers import AppointmentSerializer, DoctorSerializer,ConsultationBillSerializer #ConsultationSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    

class ConsultationBillViewSet(viewsets.ModelViewSet):
    queryset = ConsultationBill.objects.all()
    serializer_class = ConsultationBillSerializer    

# class ConsultationViewSet(Consultationviewsets.ModelViewSet):
#     queryset = Consultation.objects.all()
#     serializer_class = ConsultationSerializer
