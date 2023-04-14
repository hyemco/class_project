from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
  
  class Meta:
    model = Movie
    fields = ('title', 'description')


class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    exclude = ('user', 'movie', 'origin_comment', )
    

class ReplayForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = ('content', )
    labels = {'content': 'reply'}
  