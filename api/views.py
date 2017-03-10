from rest_pandas import PandasView
from rest_framework import serializers
from rest_framework import serializers, viewsets
from django.contrib import admin

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin.models.LogEntry
        fields = ('__all__')

class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = admin.models.LogEntry.objects.all()
    serializer_class = LogEntrySerializer