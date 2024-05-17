from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, ProductModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('', include(router.urls))
    # path('product/', ProductListCreateAPIView.as_view()),
    # path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
]

