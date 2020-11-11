from rest_framework import serializers
from .models import *

class TBGRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBGR
        fields = ('board',
                  'village',
                  'tbgrno',
                  'name')

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('boardid',
                  'boardname')

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ('boardname',
                  'villageid',
                  'villagename')
class SlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slip
        fields = ('date',
                  'tbgrno',
                  'grade',
                  'lotno',
                  'weight',
                  'price')
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ('gradeid',
                  'grade')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('name',
                  'phone')
