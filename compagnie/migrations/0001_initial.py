# Generated by Django 3.0.8 on 2020-07-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCompagnie', models.CharField(max_length=500)),
                ('adresseTana', models.CharField(max_length=500)),
                ('adresseTamatave', models.CharField(max_length=500)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('email3', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=500)),
            ],
        ),
    ]
