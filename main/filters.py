import django_filters
from django_filters import DateFilter
from .models import Test, TestItem

class TestFilter(django_filters.FilterSet):
    class Meta:
        model = Test
        exclude = ['test_time_start', 'test_time_end']
        
class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = TestItem
        exclude = ['test', 'number_of_parts']