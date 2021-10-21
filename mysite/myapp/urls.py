from django.urls import path
from .views import Home, upload


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('upload/', upload, name='upload'),
]
