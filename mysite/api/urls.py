from .views import api, transacoesList, transacoesDetail, transacoesCreate
from django.urls import path


urlpatterns = [
    path('api/', api, name='api'),
    path('api/transacoes-lista/', transacoesList, name='transacoes_lista'),
    path('api/transacoes-detalhe/<str:pk>/', transacoesDetail, name='transacoes_detalhe'),
    path('api/transacoes-criar/', transacoesCreate, name='transacoes_criar'),
]