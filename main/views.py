from django.shortcuts import render

#auth
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
#data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BusinessCardSerializer
from rest_framework.permissions import IsAuthenticated
from .models import BusinessCard

#authetication
@api_view(['POST'])
def get_tokens_for_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.filter(username=username).first()

    if user is None or not user.check_password(password):
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })


class BusinessCardListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, format=None):
        business_cards = BusinessCard.objects.all()
        serializer = BusinessCardSerializer(business_cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BusinessCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        try:
            business_card = BusinessCard.objects.get(pk=pk)
        except BusinessCard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BusinessCardSerializer(business_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        try:
            business_card = BusinessCard.objects.get(pk=pk)
            business_card.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BusinessCard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


# Create your views here.
