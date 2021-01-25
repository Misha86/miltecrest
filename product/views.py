from product.models import Product
from rest_framework import viewsets
from rest_framework import permissions
from product.serializers import ProductSerializer
from miltec.service import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ProductPagination
