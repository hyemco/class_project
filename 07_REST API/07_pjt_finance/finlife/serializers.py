from rest_framework import serializers
from .models import DepositProducts, DepositOptions


class DepositProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DepositProducts
        fields = '__all__'
    
    
class DepositOptionsSerializer(serializers.ModelSerializer):
    intr_rate = serializers.FloatField(default=-1, allow_null=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd', )