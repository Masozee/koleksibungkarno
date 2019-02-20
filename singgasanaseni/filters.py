import django_filters
from .models import perupa


class PerupaFilter(django_filters.FilterSet):
    class Meta:
        model = perupa
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['Nama', 'Panggilan']