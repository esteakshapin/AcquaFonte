from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models.fountain import Fountain, FountainUpdateModel
from .models.update import Update
from import_export.admin import ImportExportModelAdmin
from fountain.resource import FountainResource


# Register your models here.


@admin.register(Fountain)
class FountainAdmin(OSMGeoAdmin):
    list_display = ('id', 'title', 'status', 'feature', 'location', 'access')


@admin.register(FountainUpdateModel)
class FountainUpdateModelAdmin(OSMGeoAdmin):
    list_display = ('title', 'status', 'feature', 'location', 'access')


class FountainAdmin(ImportExportModelAdmin, admin.GeoModelAdmin):
    resource_class = FountainResource


# admin.site.register(Fountain, FountainAdmin)
# admin.site.register(FountainUpdateModel, admin.GeoModelAdmin)
admin.site.register(Update, admin.GeoModelAdmin)
