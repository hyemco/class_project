from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

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
  print(1111, request.user.username)
  if request.method == 'POST':
    form = MovieForm(request.POST)
    if form.is_valid():
      movie = form.save()
      return redirect('movies:detail', movie.pk)
  else:
    form = MovieForm()
  context = {
    'form': form
  }
  return render(request, 'movies/create.html', context)


@require_safe
def detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  context = {
    'movie': movie
  }
  return render(request, 'movies/detail.html', context)
  

@require_http_methods(['GET', 'POST'])
@login_required
def update(request, pk):
  movie = Movie.objects.get(pk=pk)
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
  if movie.user_id == request.user.id:
    movie.delete()
  return redirect('movies:index')