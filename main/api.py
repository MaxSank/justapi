from .models import Record
from rest_framework import viewsets, permissions
from .serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecordSerializer
