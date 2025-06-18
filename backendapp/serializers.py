from rest_framework import serializers
from .models import Staff

class LoginSerializer(serializers.Serializer):
    UserName = serializers.CharField()
    Password = serializers.CharField()

class StaffSerializer(serializers.ModelSerializer):
    RoleName = serializers.CharField(source='RoleId.RoleName', read_only=True)

    class Meta:
        model = Staff
        fields = ['StaffId', 'FullName', 'UserName', 'RoleName']
