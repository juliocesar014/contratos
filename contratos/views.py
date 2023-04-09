from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser
from .models import Contrato
from .serializer import ContratoSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    parser_class = (FileUploadParser,)
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

