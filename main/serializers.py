# serializers.py
from rest_framework import serializers
from .models import BusinessCard

class BusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCard
        fields = ['id', 'logo', 'name', 'email', 'phone_number', 'website', 'profession', 'address']
