# Generated by Django 3.1.1 on 2020-10-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobacco', '0002_tbgr_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('boardid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('boardname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('boardid', models.CharField(max_length=5)),
                ('villageid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('villagename', models.CharField(max_length=20)),
            ],
        ),
    ]