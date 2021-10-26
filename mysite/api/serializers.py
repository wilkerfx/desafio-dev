from rest_framework import serializers
from django.apps import apps


TransacoesEntity = apps.get_model('myapp',
                                  'TransacoesEntity')


class TransacoesEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransacoesEntity
        fields = '__all__'