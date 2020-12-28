# Generated by Django 3.1.4 on 2020-12-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fountain',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Not Working'), ('unknown', 'Unknown')], default='unknown', max_length=10),
        ),
    ]
