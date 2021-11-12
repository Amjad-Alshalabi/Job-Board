import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary = django_filters.NumberFilter()
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner', 'slug','image','published_at','Vacancy']      