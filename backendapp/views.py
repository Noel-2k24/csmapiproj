from django.shortcuts import render
from .serilaizers import MembershipSerializer,PatientSerializer
from rest_framework import viewsets
from.models import Membership,Patient
# Create your views here.
class MembershipViewSet(viewsets.ModelViewSet):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer