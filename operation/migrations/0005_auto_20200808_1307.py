# Generated by Django 3.0.8 on 2020-08-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_operation_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='Reference_Reception',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
