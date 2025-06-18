from rest_framework import serializers
from.models import Membership,Patient
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Membership
        fields='__all__'
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'