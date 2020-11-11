import django_filters
from .models import *
class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Slip
        fields = '__all__'
