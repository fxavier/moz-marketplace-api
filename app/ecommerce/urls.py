from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'ecommerce'

router = DefaultRouter()
router.register('products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]