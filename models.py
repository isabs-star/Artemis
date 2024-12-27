from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Outros campos personalizados, se houver

    # Modificando o 'groups' para usar related_name para evitar conflito
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Nome único para evitar conflito
        blank=True,
    )

    # Modificando o 'user_permissions' para usar related_name
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions_set',  # Nome único para evitar conflito
        blank=True,
    )

class Relato(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Use 'Usuario' here instead of 'User'
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
