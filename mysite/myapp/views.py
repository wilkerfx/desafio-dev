from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.core.files.storage import FileSystemStorage
from .models import TransacoesImportacao, TransacoesEntity, TipoTransacoesEntity
import datetime
from django.contrib import messages
from django.db.models import Count, F, Value
from django.db.models import Sum


@login_required(login_url='login')
def Home(request):

    return render(request, 'index.html',)


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        if not (uploaded_file.name.endswith(".txt")):
            messages.add_message(request, messages.ERROR,
                                 "Tipo de arquivo não suportado.")
            return render(request, 'upload.html')

        file_system = FileSystemStorage()
        file_system.delete(uploaded_file.name)
        file_system.save(uploaded_file.name, uploaded_file)
        filepath = file_system.path(uploaded_file.name)

        with open(filepath, 'r') as txt_file:
            reader = txt_file.readlines()
            lista_importacao = []
            for item in reader:
                modelo_importacao = TransacoesImportacao(
                    Tipo=str(item)[0:1],
                    Data=str(item)[1:9],
                    Valor=str(item)[9:19],
                    CPF=str(item)[19:30],
                    Cartao=str(item)[30:42],
                    Hora=str(item)[42:48],
                    Dono_da_Loja=str(item)[48:62],
                    Nome_da_loja=str(item)[62:81]
                )
                lista_importacao.append(modelo_importacao)
        txt_file.close()
        for i in lista_importacao:
            tipo_transacao = TipoTransacoesEntity.objects.get(id=i.Tipo)
            modelo_transacoes = TransacoesEntity(
                Tipo=tipo_transacao,
                Data=datetime.datetime.strptime(i.Data, '%Y%m%d'),
                Valor=(float(i.Valor) / 100.00),
                CPF=i.CPF,
                Cartao=i.Cartao,
                Hora=datetime.datetime.strptime(i.Hora, '%H%M%S').strftime('%H:%M:%S'),
                Dono_da_Loja=i.Dono_da_Loja,
                Nome_da_loja=i.Nome_da_loja,
                Total=float(tipo_transacao.Sinal+str((float(i.Valor) / 100.00)))
            )
            modelo_transacoes.save()
        file_system.delete(uploaded_file.name)
        messages.add_message(request, messages.SUCCESS,
                         'Arquivo carregado com sucesso.')
    return render(request, 'upload.html')


class TransacoesEntityListView(ListView):
    model = TransacoesEntity
    paginate_by = 3
    queryset = TransacoesEntity.objects.order_by('-Nome_da_loja')
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ValorTotal'] = TransacoesEntity.objects.aggregate(Sum('Total'))
        return context





