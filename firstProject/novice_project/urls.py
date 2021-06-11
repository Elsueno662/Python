from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='users_register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users_logout'),
    #path('', include('users.urls')),
    #path('', include('beginner.urls')),
]
