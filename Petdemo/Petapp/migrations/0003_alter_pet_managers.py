# Generated by Django 5.0.1 on 2024-01-07 10:18

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Petapp', '0002_cart'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pet',
            managers=[
                ('prod', django.db.models.manager.Manager()),
            ],
        ),
    ]
