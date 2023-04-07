# 04_pjt

## 새로 학습한 내용

- ModelForm에 조건 주기 - `widget`을 이용함

```python
GENRE_CHOICES = [
        ('코미디', '코미디'),
        ('공포', '공포'),
        ('로맨스', '로맨스'),
    ]

    genre = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=GENRE_CHOICES)
```

- update 할 때 수정 내용 다시 복구하기 - `type="Reset"` 사용

```HTML
<input tpye="Reset">
```
