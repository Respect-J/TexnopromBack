from django.urls import path
from .views import ProductListView, ProductRetrieveUpdateDelete, BrandProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='Product-get-create'),
    path('<uuid:pk>/', ProductRetrieveUpdateDelete.as_view(), name='Product-retrieve-update-delete'),
    path('brand/<uuid:brand_id>/', BrandProductListView.as_view(), name='brand-product-list'),
]