# Generated by Django 3.1 on 2020-08-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0003_auto_20200821_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactureMoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_Facture', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
