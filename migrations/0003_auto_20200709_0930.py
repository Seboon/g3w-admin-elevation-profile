# Generated by Django 2.2.13 on 2020-07-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleprofile', '0002_auto_20200709_0929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eleprodtm',
            options={'verbose_name': 'Elevation Profile DTM Layer'},
        ),
        migrations.AlterModelOptions(
            name='eleprolayer',
            options={'verbose_name': 'Elevation Profile Line Layer'},
        ),
        migrations.AlterModelOptions(
            name='eleproproject',
            options={'verbose_name': 'Elevation Profile Project'},
        ),
    ]
