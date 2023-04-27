from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import JsonResponse
from django.conf import settings
import requests

from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    deposit_base_infos = response['result']['baseList']
    for deposit_base_info in deposit_base_infos:
        serializer = DepositProductsSerializer(data=deposit_base_info)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        fin_prdt_cd = deposit_base_info['fin_prdt_cd']
        depositProduct = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    
        deposit_option_inofs = response['result']['optionList']
        for deposit_option_info in deposit_option_inofs:
            if deposit_option_info['fin_prdt_cd'] == fin_prdt_cd:
                serializer = DepositOptionsSerializer(data=deposit_option_info)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(fin_prdt_cd=depositProduct)

    return Response({'message': "okay"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        depositProducts = get_list_or_404(DepositProducts)
        serializer = DepositProductsSerializer(depositProducts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': "이미 있는 데이터거나, 데이터가 잘못 입력되었습니다."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    depositProduct = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    if request.method == 'GET':
        options = depositProduct.depositoptions_set.filter()
        serializer = DepositOptionsSerializer(options, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    best_intr_rate_option = DepositOptions.objects.order_by('-intr_rate2').first()
    target_product = best_intr_rate_option.fin_prdt_cd
    if request.method == 'GET':
        serializer_product = DepositProductsSerializer(target_product)
        serializer_option = DepositOptionsSerializer(best_intr_rate_option)
        data = {
            'deposit_product': serializer_product.data,
            'options': serializer_option.data,
        }
        return Response(data)
