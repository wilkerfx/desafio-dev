from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import UpdateView
from .views import Home, upload, TransacoesEntityListView


urlpatterns = [
    path('', Home, name='index'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='register/login.html'),
                                                name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'),
                                                name='logout'),
    path('upload/', upload, name='upload'),
    path('listagem/', TransacoesEntityListView.as_view(), name='list'),
    path('', include('register.urls')),
]
