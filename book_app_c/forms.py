from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "director", "imdb_rating"]


    def clean(self):
        cleaned_data = super(MovieForm, self).clean()
        title = cleaned_data.get('title')
        director = cleaned_data.get('director')
        imdb_rating = cleaned_data.get('imdb_rating')
        if not title and not director and not imdb_rating:
            raise forms.ValidationError('Please fill in all the required fields!')