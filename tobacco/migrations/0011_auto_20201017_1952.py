# Generated by Django 3.1.1 on 2020-10-17 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tobacco', '0010_auto_20201017_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='height',
            new_name='price',
        ),
    ]