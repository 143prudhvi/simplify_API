# Generated by Django 3.1.1 on 2020-10-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobacco', '0003_board_village'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='boardid',
            field=models.CharField(auto_created=True, max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='village',
            name='villageid',
            field=models.CharField(auto_created=True, max_length=5, primary_key=True, serialize=False),
        ),
    ]
