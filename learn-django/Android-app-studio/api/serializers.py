from rest_framework.serializers import ModelSerializer
from .models import AndroidApp

class AndroidAppSerializer(ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = ['id', 'name', 'points', 'url']