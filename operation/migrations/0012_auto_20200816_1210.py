# Generated by Django 3.0.8 on 2020-08-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0011_auto_20200815_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='TotalFacture',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
