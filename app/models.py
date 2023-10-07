from django.db import models

# Create your models here.
class tasks_db(models.Model):
    task = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    