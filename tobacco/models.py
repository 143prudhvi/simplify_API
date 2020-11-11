from datetime import datetime
from django.db import models

# Create your models here.

class TBGR(models.Model):
    board = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    tbgrno = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)

class Board(models.Model):
    boardid = models.AutoField(primary_key=True, auto_created=True)
    boardname = models.CharField(max_length=20)

class Village(models.Model):
    boardname = models.CharField(max_length=20)
    villageid = models.AutoField(primary_key=True, auto_created=True)
    villagename = models.CharField(max_length=20)

class Slip(models.Model):
    date = models.DateTimeField(default=datetime.now())
    tbgrno = models.CharField(max_length=20)
    grade = models.CharField(max_length=5)
    lotno = models.CharField(max_length=20, primary_key=True)
    weight = models.DecimalField(decimal_places=3,max_digits=10)
    price = models.DecimalField(decimal_places=3,max_digits=10)

class Grades(models.Model):
    gradeid = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=5)

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(primary_key=True)
