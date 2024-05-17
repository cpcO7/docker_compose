from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'slug'


class ProductListModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'created_at', 'updated_at', 'description'

    def to_representation(self, instance: Product):
        represent = super().to_representation(instance)
        represent['category'] = CategoryModelSerializer(instance.category).data
        return represent


class ProductDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'updated_at',

    def to_representation(self, instance: Product):
        represent = super().to_representation(instance)
        represent['category'] = CategoryModelSerializer(instance.category).data
        return represent
