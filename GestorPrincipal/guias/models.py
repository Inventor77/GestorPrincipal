from django.db import models

class Guias(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

