# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TransacoesEntitySerializer
from .serializers import TransacoesEntity


@api_view(['GET'])
def api(request):
    api_urls = {
        'List': '/transacoes-lista/',
        'Detail View': '/transacoes-detalhe/<str:pk>/',
        'Create': '/transacoes-criar/',
    }
    return Response(api_urls)


@api_view(['GET'])
def transacoesList(request):
    transacoes = TransacoesEntity.objects.all()
    serializer = TransacoesEntitySerializer(transacoes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def transacoesDetail(request, pk):
    transacoes = TransacoesEntity.objects.get(id=pk)
    serializer = TransacoesEntitySerializer(transacoes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def transacoesCreate(request):
    serializer = TransacoesEntitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)