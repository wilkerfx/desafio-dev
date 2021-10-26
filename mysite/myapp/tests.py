from django.test import TestCase
from .models import TransacoesImportacao, TransacoesEntity,TipoTransacoesEntity
from django.utils import timezone
import datetime

list = [TransacoesImportacao]

# Importar os dados do texto e incluir na nossa lista de transacoes
with open('cnab.txt') as f:
    lines = f.readlines()
    for item in lines:
        model = TransacoesImportacao
        model.Tipo = item[1:1]
        model.Data = item[2:9]
        model.Valor = item[10:19]
        model.CPF = item[20:30]
        model.Cartao = item[31:42]
        model.Hora= item[43:48]
        model.Dono_da_Loja=item[49:62]
        model.Nome_da_loja = item[63:81]
        list.append(model)

# Exportar os dados da lista para a nossa entidade na base de dados
for transa in list:
    model = TransacoesEntity
    tipo = TipoTransacoesEntity.objects.get(pk=transa.tipo)
    model.Tipo = tipo
    model.Data = datetime.datetime.strftime('%d/%m/%y')
    model.Valor = float(transa.valor)
    model.CPF = transa.CPF
    model.Cartao = transa.cartao
    model.Hora = datetime.datetime.strptime(str(transa.Hora), '%H:%M:%S')
    model.Dono_da_Loja = transa.Dono_da_Loja
    model.Nome_da_loja = transa.Nome_da_loja
    model.save()









'''
    modelo_transacoes = TransacoesEntity
    #   modelo_transacoes = TipoTransacoesEntity.objects.get(transacao.Tipo)
    modelo_transacoes.Tipo = modelo_importacao.Tipo
    #   modelo_transacoes.Data = datetime.datetime.strftime(str(transacao.Data, '%d%m%Y'))
    modelo_transacoes.Valor = modelo_importacao.Valor
    modelo_transacoes.CPF = modelo_importacao.CPF
    modelo_transacoes.Cartao = modelo_importacao.Cartao
    #   modelo_transacoes.Hora = datetime.datetime.strptime(str(transacao.Hora), '%H:%M:%S')
    modelo_transacoes.Dono_da_Loja = modelo_importacao.Dono_da_Loja
    modelo_transacoes.Nome_da_loja = modelo_importacao.Nome_da_loja
    modelo_transacoes.save'''




from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
# from .forms import UploadForm
from .models import TransacoesImportacao, TransacoesEntity, TipoTransacoesEntity
import datetime
import os


class Home(TemplateView):
    template_name = "index.html"


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print(uploaded_file.name)
        print(uploaded_file.size)
        file_system = FileSystemStorage()
        file_system.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')


def listagem(request):
    path = "C:/Users/painkiller/PycharmProjects/wilker_bycoders_test/mysite/media"
    os.chdir(path)
    lista_importacao = []
    with open('CNAB.txt', 'r') as txt_file:
        reader = txt_file.readlines()
        for item in reader:
            modelo_importacao = TransacoesImportacao
            modelo_importacao.Tipo = str(item)[0:1]
            modelo_importacao.Data = str(item)[1:9]
            modelo_importacao.Valor = str(item)[9:19]
            modelo_importacao.CPF = str(item)[19:30]
            modelo_importacao.Cartao = str(item)[30:42]
            modelo_importacao.Hora = str(item)[42:48]
            modelo_importacao.Dono_da_Loja = str(item)[48:62]
            modelo_importacao.Nome_da_loja = str(item)[62:81]
            '''print(modelo.Tipo)
            print(modelo.Data)
            print(modelo.Valor)
            print(modelo.CPF)
            print(modelo.Cartao)
            print(modelo.Hora)
            print(modelo.Dono_da_Loja)
            print(modelo.Nome_da_loja)'''
            lista_importacao.append(modelo_importacao)
        txt_file.close()
        for transacao in lista_importacao:
            modelo_transacoes = TransacoesEntity
        #   modelo_transacoes = TipoTransacoesEntity.objects.get(transacao.Tipo)
        #   modelo_transacoes.Tipo = tipo_transacao
        #   modelo_transacoes.Data = datetime.datetime.strftime(str(transacao.Data, '%d%m%Y'))
            modelo_transacoes.Valor = float(transacao.Valor)
            modelo_transacoes.CPF = transacao.CPF
            modelo_transacoes.Cartao = transacao.Cartao
        #   modelo_transacoes.Hora = datetime.datetime.strptime(str(transacao.Hora), '%H:%M:%S')
            modelo_transacoes.Dono_da_Loja = transacao.Dono_da_Loja
            modelo_transacoes.Nome_da_loja = transacao.Nome_da_loja

    #transacoes_modelo_final = modelo_transacoes.objects.all()[:10]
    transacoes_modelo_final = modelo_transacoes.CPF[:10]

    context = {
        'transacoes_modelo_final': transacoes_modelo_final
    }
    return render(request, 'list.html', context)




_diskspace_gb_vswap = models.DecimalField(db_column="diskspace_gb_vswap", decimal_places=2 , max_digits=10)

@property

def diskspace_gb_vswap(self):

    return self._diskspace_gb_vswap

@diskspace_gb_vswap.setter

def diskspace_gb_vswap(self , value):

    self._diskspace_gb_vswap = self.diskspacegb * 1.5