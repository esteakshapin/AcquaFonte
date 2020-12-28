from django.contrib import admin

# Register your models here.
from .models.fountain import Fountain

admin.site.register(Fountain)