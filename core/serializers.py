from rest_framework import serializers
from .models import ReservaPabellon

class ReservaPabellonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaPabellon
        fields = '__all__'
