# Generated by Django 2.0 on 2017-12-29 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0002_restaurant_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='RestaurantLocation',
        ),
    ]
