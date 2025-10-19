from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField('Título', max_length=150)
    content = models.TextField('Contenido', blank=True)
    created_at = models.DateTimeField('Creado el', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.CharField(max_length=160, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("profile-detail", kwargs={"pk": self.pk})