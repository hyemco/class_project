# DB 설계를 활용한 REST API 설계



## 새롭게 학습한 내용

1. message 담아서 response하기
```python
return Response({'message': "okay"}, status=status.HTTP_200_OK)
```

<br>

2. serializer하면서 default 값 설정하기
- data가 들어올 때 이미 null값으로 들어오고 있으므로 **null 값을 허용**해준 뒤, null 값이면 default 값으로 설정되게 해줌
```python
# serializers.py
class DepositOptionsSerializer(serializers.ModelSerializer):
    intr_rate = serializers.FloatField(default=-1, allow_null=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd', )


# models.py
intr_rate = models.FloatField(null=True)
```

<br>

3. serializer한 여러 데이터 한 번에 response하기
```python
serializer_product = DepositProductsSerializer(target_product)
        serializer_option = DepositOptionsSerializer(best_intr_rate_option)
        data = {
            'deposit_product': serializer_product.data,
            'options': serializer_option.data,
        }
        return Response(data)
```