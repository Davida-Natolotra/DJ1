# Generated by Django 3.0.7 on 2020-08-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0005_factureoperation_ref'),
    ]

    operations = [
        migrations.CreateModel(
            name='BLMoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_BL', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='facturemoto',
            name='Num_Facture',
            field=models.IntegerField(default=0, null=True),
        ),
    ]