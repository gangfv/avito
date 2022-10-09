from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from django.urls import reverse


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    middle_name = models.CharField(null=True, blank=True, max_length=100, verbose_name='Отчество')
    vip = models.BooleanField(default=False, verbose_name='VIP')

    def __str__(self):
        return self.username if self.username else self.email

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
