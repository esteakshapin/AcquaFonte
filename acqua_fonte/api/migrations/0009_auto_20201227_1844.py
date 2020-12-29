# Generated by Django 3.1.4 on 2020-12-27 18:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201227_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fountain',
            name='feature',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'Bottle Refiller'), (1, 'Kid Friendly'), (2, 'Accesible'), (3, 'Pet Fiendly')], max_length=7, null=True),
        ),
    ]