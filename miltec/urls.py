"""miltec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:    path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# from django.conf.urls.static import static
from rest_framework import routers
from buyer import views as _buyer
from menu import views as _menu
from product import views as _product

router = routers.DefaultRouter()
router.register(r'users', _buyer.UserViewSet)
router.register(r'groups', _buyer.GroupViewSet)

router.register(r'categories', _menu.CategoryViewSet)
router.register(r'items', _menu.ItemViewSet)

router.register(r'products', _product.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/menu', include('menu.urls'), name='menu')
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL,
#                       document_root=settings.MEDIA_ROOT)
