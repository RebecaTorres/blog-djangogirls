from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(
            default=timezone.now
            )
    data_publicacao = models.DateTimeField(
            blank=True, null=True
            )

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    def _str_(self):
        return self.titulo
