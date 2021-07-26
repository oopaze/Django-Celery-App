from datetime import time

from django.db import models
from django.urls.base import reverse



# Create your models here.
class Task(models.Model):
    STATUS = (
        ("registrada", "Registrada"),
        ("em_espera", "Em Espera"),
        ("em_execucao", "Em Execução"),
        ("finalizada", "Finalizada"),
    )

    titulo = models.CharField("Título", max_length=50)
    descricao = models.TextField("Descrição")
    tempo_espera = models.PositiveIntegerField("Tempo de espera", default=3)
    status = models.CharField(max_length=20, choices=STATUS, default="registrada")

    def get_absolute_url(self):
        return reverse("task-detail", args=[self.id])

    @property
    def status_display(self):
        return {
            "registrada": "Registrada",
            "em_espera": "Em Espera",
            "em_execucao": "Em Execução",
            "finalizada": "Finalizada"
        }[self.status]
