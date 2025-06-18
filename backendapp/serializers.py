# from rest_framework import serializers
# from.models import*
from rest_framework import serializers
from .models import Role,Staff,Specialization,Doctor
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specialization
        fields='__all__'
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'