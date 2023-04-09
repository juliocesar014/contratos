from rest_framework import viewsets, permissions, status
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import NotFound
from .models import Contrato
from .serializer import ContratoSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    parser_class = (FileUploadParser,)
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_object(self):
        try:
            obj = super().get_object()
            self.check_object_permissions(self.request, obj)
            return obj
        except Contrato.DoesNotExist:
            raise NotFound()

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise NotFound()
        return super().create(request, *args, **kwargs)
