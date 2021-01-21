# Generated by Django 3.1.5 on 2021-01-21 12:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20210121_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='guest_card',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='host_card',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
