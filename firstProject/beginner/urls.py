from django.urls import path
#from book_app import views as book_app_views
from book_app_c import views as book_app_c_views


urlpatterns = [
    # The commented routes are for the app book_app
    # Function based view is implemented in book_app
    #path('', book_app_views.display, name='book_display'),
    #path('add', book_app_views.add, name='book_add'),
    #path('update/<id>', book_app_views.update, name='book_update'),
    #path('delete/<id>', book_app_views.delete, name='book_delete'),

    # The commented routes are for the app book_app_c
    # Class based view is implemented in book_app_c
    #path('', book_app_c_views.MovieListView.as_view(), name='movie_show'),
    #path('movie/add/', book_app_c_views.MovieCreateView.as_view(), name='movie_add'),
    #path('movie/<pk>/update/', book_app_c_views.MovieUpdateView.as_view(), name='movie_update'),
    #path('movie/<pk>/delete/', book_app_c_views.MovieDeleteView.as_view(), name='movie_delete'),
]

