import django_filters
from django_filters import CharFilter
from .models import *

class MarageFilter(django_filters.FilterSet):
    State = CharFilter(field_name='state', lookup_expr='icontains')
    City = CharFilter(field_name='city', lookup_expr='icontains')
    class Meta:
        model = Marage
        fields = '__all__'
        exclude = ['profile_pic', 'referance_person_detail','house_bill_address_pic','cnic_front_pic','cnic_back_pic','facebook_id_link']