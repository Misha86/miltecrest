from product.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['id', 'title', 'url', 'image', 'image_large']
        depth = 1
