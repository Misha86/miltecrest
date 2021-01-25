from menu.models import Item, Category

from product.serializers import ProductSerializer

from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict


class ParentRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterReviewListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super(FilterReviewListSerializer, self).to_representation(data)


class ItemSerializer(serializers.ModelSerializer):
    children = ParentRelatedField(many=True, read_only=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'url', 'children', 'products']
        # fields = ['id', 'title', 'url', 'children']
        list_serializer_class = FilterReviewListSerializer
        depth = 1


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
