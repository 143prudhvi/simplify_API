# Generated by Django 3.1.1 on 2020-10-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobacco', '0007_auto_20201017_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='boardname',
            field=models.CharField(max_length=20),
        ),
    ]
