# 영화 06_pjt 관계형 데이터베이스 설계 


## 새롭게 학습한 내용

1.  '싫어요 기능' 구현

- '좋아요 기능'과 맥락은 동일
- 좋아요가 눌러진 상태에서 싫어요를 누르면 좋아요 누른게 취소되어야 함
- 반대로, 싫어요가 눌러진 상태에서 좋아요를 누르면 싫어요 누른 것 취소

```python
@require_POST
def likes(request, pk):
 if request.user.is_authenticated:
   movie = Movie.objects.get(pk=pk)
   if movie.like_users.filter(pk=request.user.pk).exists():
     movie.like_users.remove(request.user)
   else:
     movie.like_users.add(request.user)
     # 싫어요 취소
     if movie.hate_users.filter(pk=request.user.pk).exists():
       movie.hate_users.remove(request.user)
   return redirect('movies:index')
 return redirect('accounts:login')
```

2.  대댓글 기능 구현

- comment와 1:N 관계 맺음
- 원댓글(origin_comment)이 있는지 없는지로 댓글과 대댓글 구분

models.py

```python
from django.db import models

class Comment(models.Model):
 origin_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name='comments')
```

views.py

```python
@require_safe
def detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  comment_form = CommentForm()
  # 대댓글 폼 추가
  reply_form = ReplayForm()
  comments = Comment.objects.filter(movie=movie)
  context = {
    'movie': movie,
    'comment_form': comment_form,
    'reply_form': reply_form,
    'comments': comments,
  }
  return render(request, 'movies/detail.html', context)


# 대댓글 기능 추가
@require_POST
def recomments(request, movie_pk, comment_pk):
  if request.user.is_authenticated:
    movie = Movie.objects.get(pk=movie_pk)
    comment = Comment.objects.get(pk=comment_pk)
    comment_form = ReplayForm(request.POST)
    if comment_form.is_valid():
      recomment = comment_form.save(commit=False)
      recomment.user = request.user
      recomment.movie = movie
      # origin_comment에 comment 추가 해주기
      recomment.origin_comment = comment
      recomment.save()
      return redirect('movies:detail', movie.pk)
  return redirect('accounts:login')
```

detail.html

```html
{% for comment in comments %}
<!-- origin_comment 값의 유무로 댓글과 대댓글 구분 -->
{% if comment.origin_comment == Null %}
<ul>
  <div class="d-flex">
    <li>{{ comment.content }}</li>
    {% if request.user == comment.user %}
    <form
      class="ms-3"
      action="{% url 'movies:comments_delete' movie.pk comment.pk %}"
      method="POST"
    >
      {% csrf_token %}
      <input type="submit" value="DELETE" />
    </form>
    {% endif %}

    <!-- 대댓글 작성 form -->
    <form
      class="ms-4"
      action="{% url 'movies:recomments' movie.pk comment.pk %}"
      method="POST"
    >
      {% csrf_token %} {{reply_form}}
      <input type="submit" value="답글" />
    </form>

    <!-- 대댓글 목록 -->
    {% for reply in comment.comments.all %}
    <ul>
      <li>{{ reply.content }}</li>
    </ul>
    {% endfor %}
  </div>
</ul>
{% endif %} {% endfor %}
```

<br><br>

## 아쉬운 점

- 대댓글 기능 구현을 하면서 변수명이 통일되지 못했다
- origin_comment 값의 유무로 댓글과 대댓글을 구분하는 작업을 html에서 해뒀는데, views.py에서 댓글과 대댓글로 구분해서 넘겼다면 더 좋았을 것 같다.