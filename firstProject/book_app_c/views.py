from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Movie
from django.contrib.messages.views import SuccessMessageMixin


class MovieCreateView(SuccessMessageMixin, CreateView):
    model = Movie
    fields = ["title", "director", "imdb_rating"]
    template_name_suffix = '_create_form'
    success_url = "/"
    success_message = "Movie was added successfully"


class MovieListView(ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    model = Movie
    fields = ["title", "director", "imdb_rating"]
    template_name_suffix = '_update_form'
    success_url = "/"
    success_message = "Movie was updated successfully"


class MovieDeleteView(SuccessMessageMixin, DeleteView):
    model = Movie
    success_url = "/"