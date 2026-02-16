from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BalanceActionSerializer(serializers.Serializer):
    amount = serializers.FloatField(min_value=0.01)

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"