# Generated by Django 3.0.8 on 2020-08-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caisseTana', '0002_auto_20200824_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='depense',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='caisse',
            name='recette',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=20, null=True),
        ),
    ]