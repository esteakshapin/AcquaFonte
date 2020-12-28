from django.contrib import admin

# Register your models here.
from .models.fountain import Fountain
from .models.update import Update

admin.site.register(Fountain)
admin.site.register(Update)
