from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductListModelSerializer, ProductDetailModelSerializer
from django.core.cache import cache


class CategoryListCreateAPIView(ListAPIView):
    queryset = Category.objects.order_by('id')
    serializer_class = CategoryModelSerializer


class CategoryRetrieveUpdateDestroyAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductListModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['price', 'created_at']

    # v1
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = 'category', 'slug'

    # v2
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = {
    #     "price": ['lte']
    #     # "slug": ["contains"],
    #     # "description": ["contains"],
    # }
    #
    # # v3
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
    # ordering_fields = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListModelSerializer
        return ProductDetailModelSerializer

# class ProductListCreateAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductListModelSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = 'category',
#
#
# class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailModelSerializer
