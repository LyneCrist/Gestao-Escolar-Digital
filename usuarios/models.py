from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('pais', 'Pais'),
        ('professor', 'Professor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.username