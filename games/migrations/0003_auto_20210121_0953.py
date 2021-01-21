# Generated by Django 3.1.5 on 2021-01-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20210121_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='guest_card',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='5', max_length=2),
        ),
        migrations.AlterField(
            model_name='game',
            name='host_card',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='5', max_length=2),
        ),
    ]