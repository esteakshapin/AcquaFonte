from django.contrib import admin
from .models.fountain import Fountain, FountainUpdateModel
from .models.update import Update

# Register your models here.
admin.site.register(Fountain)
admin.site.register(FountainUpdateModel)
admin.site.register(Update)
