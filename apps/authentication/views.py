from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer

from .serializers import BalanceActionSerializer
from .models import User

# Deposit endpoint
@extend_schema(
    request=BalanceActionSerializer,
    responses={200: dict}
)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def deposit(request, pk):
    if request.user.pk != pk:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = get_object_or_404(User, pk=pk)
    serializer = BalanceActionSerializer(data=request.data)

    if serializer.is_valid():
        try:
            user.deposit(serializer.validated_data['amount'])
            return Response(
                {"balance": user.balance},
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Withdraw endpoint
@extend_schema(
    request=BalanceActionSerializer,
    responses={200: dict}
)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def withdraw(request, pk):
    if request.user.pk != pk:
        return Response(status=status.HTTP_403_FORBIDDEN)
        
    user = get_object_or_404(User, pk=pk)
    serializer = BalanceActionSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            user.withdraw(serializer.validated_data['amount'])
            return Response(
                {"balance": user.balance},
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# JWT view
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer