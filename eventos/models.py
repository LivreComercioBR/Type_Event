from django.db import models
from type_event_app.models import User


class Evento(models.Model):
    criador = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='evento_do_usuario')
    nome = models.CharField(max_length=200)
    participantes = models.ManyToManyField(
        User, related_name="evento_participante", blank=True)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horaria = models.IntegerField()
    logo = models.FileField(upload_to="logos")

    # paleta de cores
    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)

    def __str__(self):
        return self.nome
