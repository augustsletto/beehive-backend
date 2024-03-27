from django.urls import path
from base import views

urlpatterns = [
    path('api/products/', views.ProductList.as_view()),
    path('api/products/<int:pk>/', views.ProductDetail.as_view()),
]
