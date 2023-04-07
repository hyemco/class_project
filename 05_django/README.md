# 05_pjt. 사용자 인증 기반 DB 설계

### 학습 내용
- CRUD(회원/게시글)
- ModelForm
- Django decorators로 method 제한하기

<br>

### 새롭게 배운 것
1. 로그인 한 회원에게만 권한 주기
```python
from django.contirb.auth.decorators import login_required


# 아래 데코레이터를 이용하면 로그인 하지 않은 경
# 우 로그인 페이지로,
# 로그인한 경우 해당 함수 실행
@login_required
def create(request):
  pass
```

p.s 원래 시도했던 방법
```python
def create(request):
  if request.user.is_authenticated: # 로그인 했으면 함수 실행
    pass
  else: # 로그인하지 않았으면 로그인 페이지로 이동
    return redirect('accounts:login')
```
<br>
<br>

2. 자신의 글만 수정/삭제


<br>
movies.models.py

```python
# DB관계 변경, Movie 모델에서 User 모델의 id 외래키참조
from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

<br>
movies.forms.py

```python
class MovieForm(forms.ModelForm):
  
  class Meta:
    model = Movie
    # 폼 필드에 user_id 제외한 필드만 보이게 설정
    fields = ('title', 'description')
```

<br>
movies.views.py

```python
@require_POST
@login_required
def delete(request, pk):
  movie = Movie.objects.get(pk=pk)
  # 게시글 작성 유저 아이디와 로그인한 유저 아이디 비교
  if movie.user_id == request.user.id:
    movie.delete()
  return redirect('movies:index')
```

<br>

### 해결 못한 것
- 자신의 글만 수정/삭제가능하도록 설정후 다른 사람이 수정/삭제 버튼을 눌렀을 때 알림 팝업창 같은 것이 필요하다고 느낌