from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm, ReplayForm

from django.views.decorators.http import require_safe, require_POST, require_http_methods
# 로그인 인증
from django.contrib.auth.decorators import login_required


@require_safe
def index(request):
  movies = Movie.objects.all()
  context = {
    'movies': movies,
  }
  return render(request, 'movies/index.html', context)
  

@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = MovieForm(request.POST)
      if form.is_valid():
        movie = form.save(commit=False)
        movie.user = request.user
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
      form = MovieForm()
    context = {
      'form': form
    }
    return render(request, 'movies/create.html', context)
  return redirect('accounts:login')


@require_safe
def detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  comment_form = CommentForm()
  reply_form = ReplayForm()
  comments = Comment.objects.filter(movie=movie)
  context = {
    'movie': movie,
    'comment_form': comment_form,
    'reply_form': reply_form,
    'comments': comments,
  }
  return render(request, 'movies/detail.html', context)
  

@require_http_methods(['GET', 'POST'])
@login_required
def update(request, pk):
  movie = Movie.objects.get(pk=pk)
  if request.user == movie.user:
    if request.method == 'POST':
      form = MovieForm(request.POST, instance=movie)
      if form.is_valid():
        form.save()
        return redirect('movies:detail', pk=movie.pk)
    else:
      form = MovieForm(instance=movie)
  context = {
    'form': form,
    'movie': movie
  }
  return render(request, 'movies/update.html', context)


@require_POST
@login_required
def delete(request, pk):
  movie = Movie.objects.get(pk=pk)
  if request.user == movie.user:
    movie.delete()
  return redirect('movies:index')


@require_POST
def comments_create(request, pk):
  if request.user.is_authenticated:
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.user = request.user
      comment.movie = movie
      comment.save()
      return redirect('movies:detail', movie.pk)
  return redirect('accounts:login')


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
      recomment.origin_comment = comment
      recomment.save()
      return redirect('movies:detail', movie.pk)
  return redirect('accounts:login')


@require_POST
def comments_delete(request, movie_pk, comment_pk):
  if not request.user.is_authenticated:
    return redirect('accounts:login')
  comment = Comment.objects.get(pk=comment_pk)
  if request.user == comment.user:
    comment.delete()
  return redirect('movies:detail', movie_pk)


@require_POST
def likes(request, pk):
  if request.user.is_authenticated:
    movie = Movie.objects.get(pk=pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
      movie.like_users.remove(request.user)
    else:
      movie.like_users.add(request.user)
      if movie.hate_users.filter(pk=request.user.pk).exists():
        movie.hate_users.remove(request.user)
    return redirect('movies:index')
  return redirect('accounts:login')


@require_POST
def hates(request, pk):
  if request.user.is_authenticated:
    movie = Movie.objects.get(pk=pk)
    if movie.hate_users.filter(pk=request.user.pk).exists():
      movie.hate_users.remove(request.user)
    else:
      movie.hate_users.add(request.user)
      if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    return redirect('movies:index')
  return redirect('accounts:login')