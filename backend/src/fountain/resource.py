from import_export import resources
from .models import Fountain
from import_export.fields import Field

from django.contrib.gis.geos import Point

import datetime
from django.utils.timezone import is_aware, make_aware

import re

from fountain.utils.coords_to_address import coords_to_address


class FountainResource(resources.ModelResource):
    coords = Field(attribute='coords', column_name='fountain_coordinates')

    class Meta:
        model = Fountain
        # skip_unchanged = True

    def dehydrate_coords(self, fountain):
        return '(%s, %s)' % (fountain.coords.x, fountain.coords.y)

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        super().before_import(dataset, using_transactions, dry_run, **kwargs)
        headers = dataset.headers
        headers.append('title')
        for i in headers:
            if i == 'the_geom':
                headers[headers.index(i)] = 'fountain_coordinates'
            if i == 'GIS_EDT_DT':
                headers[headers.index(i)] = 'last_updated'

    def before_import_row(self, row, row_number=None, **kwargs):
        super().before_import_row(row, row_number, **kwargs)

        coords = row['fountain_coordinates']
        coords = re.sub('POINT ', '', coords)
        coords = re.sub('\\(', '', coords)
        coords = re.sub('\\)', '', coords)
        coords = re.split('\s', coords)
        coords = Point(float(coords[0]), float(coords[1]))
        row[coords] = coords

        coords_to_address(coords.y, coords.x)

        date = row['last_updated']
        date_time_obj = datetime.datetime.strptime(
            date, '%m/%d/%Y %H:%M:%S %p +%f')
        if not is_aware(date_time_obj):
            date_time_obj = make_aware(date_time_obj)
        row['last_updated'] = date_time_obj
