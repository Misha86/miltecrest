from menu.models import Item, Category
from rest_framework import viewsets
from rest_framework import permissions
from menu.serializers import ItemSerializer, CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

# class ItemViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows items to be viewed or edited.
#     """
#     queryset = Item.objects.all().order_by('id')
#     serializer_class = ItemSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class CategoryViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows category to be viewed or edited.
#     """
#     queryset = Category.objects.all().order_by('id')
#     serializer_class = CategorySerializer
#     permission_classes = [permissions.IsAuthenticated]
