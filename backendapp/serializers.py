from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
   class Meta: #provide meta data to model class
       model = Consultation
       fields = '__all__'