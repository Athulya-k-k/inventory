# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('record_sale/<int:product_id>/', views.record_sale, name='record_sale'),
    path('best_selling_products/', views.best_selling_products, name='best_selling_products'),
]

