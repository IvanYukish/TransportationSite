from django.db import models
from django.contrib.auth.models import AbstractUser

from phone_field import PhoneField


# Create your models here.

class CustomUser(AbstractUser):
    NOT_SENT = 'NS'
    SENT = 'S'
    IN_PROCESS = 'PR'
    ACCEPTED = 'AC'

    STATUS_CHOICES = (
        (NOT_SENT, 'not sent'),
        (SENT, 'sent'),
        (IN_PROCESS, 'process'),
        (ACCEPTED, 'accepted')
    )

    email = models.EmailField(max_length=254,
                              verbose_name='email address', unique=True)
    phone_number = PhoneField(help_text='Номер телефону')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,
                              default=NOT_SENT)

    def __str__(self):
        return self.username + '  -  ' + self.email

