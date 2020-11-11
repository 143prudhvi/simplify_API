# Generated by Django 3.1.1 on 2020-10-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobacco', '0012_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='card',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
