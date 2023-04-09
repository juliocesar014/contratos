from django.db import models

class Contrato(models.Model):
    nome = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='contratos/pastacontratos/')
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.usuario}"