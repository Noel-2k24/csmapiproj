from rest_framework import viewsets
from .models import Consultation
from .serializers import ConsultationSerializer
from django.contrib.auth.models import Group

class CounsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer