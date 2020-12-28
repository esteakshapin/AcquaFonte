from django.db import models
from .models import Fountain

class Update(models.Model):
    fountain_original = models.ForeignKey(Fountian, 
                                          on_delete=models.CASCADE, 
                                          related_name='fountian_updates')
    