# inventory/urls.py
from django.urls import path
from inventory import views

urlpatterns = [
    path("dash/", views.index, name="dash"),
    path("products/", views.products, name="products"),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/low_stock/', views.low_stock_products, name='low_stock_products'),
    path("orders/", views.orders, name="orders"),
        path('orders/download_sales_data/', views.download_sales_data, name='download_sales_data'),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
]
