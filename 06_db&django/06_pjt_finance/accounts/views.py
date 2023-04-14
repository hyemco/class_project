from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('boards:index')
  else:
    form = AuthenticationForm()
  context = {'form': form,}
  return render(request, 'accounts/login.html', context)


@require_http_methods(["GET"])
def logout(request):
  auth_logout(request)
  return redirect('boards:index')


@require_http_methods(["GET", "POST"])
def signup(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('boards:index')
  else:
    form = CustomUserCreationForm()
  context = {'form': form,}
  return render(request, 'accounts/signup.html', context)


@require_http_methods(["GET"])
def profile(request, user_pk):
  person = get_user_model().objects.get(pk=user_pk)
  context = {'person': person}
  return render(request, 'accounts/profile.html', context)
  

@require_http_methods(["POST"])
def follow(request, user_pk):
  if request.user.is_authenticated:
    person = get_user_model().objects.get(pk=user_pk)
    if request.user != person:
      if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
      else:
        person.followers.add(request.user)
    return redirect('accounts:profile', person.pk)
  return redirect('accounts:login')