import django_filters
from django_filters import DateFilter, CharFilter
from .models import Test, TestItem

class TestFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = 'test_date', lookup_expr = 'gte', label = 'מתאריך')
    end_date = DateFilter(field_name = 'test_date', lookup_expr = 'lte', label = 'עד תאריך')
    notes = CharFilter(field_name = 'notes', lookup_expr = 'icontains', label = 'הערות')
    aircraft = CharFilter(field_name = 'aircraft', lookup_expr = 'icontains', label = 'כלי טיס/מכלול')
    class Meta:
        model = Test
        fields = [
            'department',
            'test_location',
            'aircraft_id',
            'findings',
            'tester',
            'checker'
        ]
        
class ItemFilter(django_filters.FilterSet):
    description = CharFilter(field_name = 'part_description', lookup_expr = 'icontains', label = 'תיאור פריט')
    class Meta:
        model = TestItem
        fields = [
            'test_method',
            'item_id',
            'tag_number'
        ]