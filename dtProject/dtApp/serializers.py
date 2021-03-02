from .models import UserProfile
from rest_framework import routers, serializers, viewsets

class UserProfile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'