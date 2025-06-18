from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Staff
from .serializers import LoginSerializer, StaffSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                staff = Staff.objects.get(UserName=serializer.validated_data['UserName'], IsActive=True)
                if check_password(serializer.validated_data['Password'], staff.Password):
                    refresh = RefreshToken.for_user(staff)
                    return Response({
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                        'user': StaffSerializer(staff).data
                    })
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Staff.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
