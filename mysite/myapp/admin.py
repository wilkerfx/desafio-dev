from django.contrib import admin
from .models import TransacoesImportacao, TransacoesEntity, TipoTransacoesEntity


admin.site.register(TipoTransacoesEntity)
admin.site.register(TransacoesEntity)
