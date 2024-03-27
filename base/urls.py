from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.getProducts.as_view(), name="products"),
    path('products/<str:pk>/', views.getProduct.as_view(), name="product"),
]
