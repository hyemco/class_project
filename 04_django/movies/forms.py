from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0,
            }),
    )

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

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0,
                'max': 5,
                'step': 0.5,
            }),
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }),
    )
    
    class Meta:
        model = Movie
        fields = '__all__'