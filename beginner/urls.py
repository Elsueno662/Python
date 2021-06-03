from django.urls import path
#from book_app import views as book_app_views
from book_app_c import views as book_app_c_views


urlpatterns = [
    # The commented routes are for the app book_app
    # Function based view is implemented in book_app
    #path('', book_app_views.display, name='display'),
    #path('add', book_app_views.add, name='add'),
    #path('update/<id>', book_app_views.update, name='update'),
    #path('delete/<id>', book_app_views.delete, name='delete'),

    # The uncommented routes are for the app book_app_c
    # Class based view is implemented in book_app_c
    path('', book_app_c_views.MovieListView.as_view(), name='movie-show'),
    path('movie/add/', book_app_c_views.MovieCreateView.as_view(), name='movie-add'),
    path('movie/<pk>/update/', book_app_c_views.MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<pk>/delete/', book_app_c_views.MovieDeleteView.as_view(), name='movie-delete'),
]

