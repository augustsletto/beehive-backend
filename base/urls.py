from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.get_products, name="products"),
    path('products/<str:pk>/', views.get_product, name="product"),
    path('products/create/', views.create_product, name="create_product"),
    path('products/update/<str:pk>/', views.update_product, name="update_product"),
    path('products/delete/<str:pk>/', views.delete_product, name="delete_product"),
]
