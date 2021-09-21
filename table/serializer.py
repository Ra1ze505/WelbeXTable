from rest_framework import serializers

from .models import *

class TableDerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'