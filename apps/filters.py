from django_filters import FilterSet, NumberFilter, CharFilter

from apps.models import Product


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    word = CharFilter(method='filter_word')

    class Meta:
        model = Product
        fields = ['category', 'word']

    def filter_word(self, queryset, name, value):
        return queryset.filter(category__name__icontains=value)
