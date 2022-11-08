from django.db import models


class User(models.Model):
    login = models.CharField(max_length=100, unique=True, blank=False)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    password_hash = models.CharField(max_length=500, blank=False)
    img = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

    main_address = models.CharField(max_length=500, blank=True)
    favourites = models.JSONField()
    balance = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)  # Создан
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('login', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login

# Create your models here.
