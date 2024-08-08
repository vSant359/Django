from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    speciality = models.IntegerField(max_length=100)  # Campo especialidade