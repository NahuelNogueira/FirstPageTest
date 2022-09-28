from django.urls import path

from . import views

app_name="cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name="add"),
    path('delete/<int:product_id>/', views.delete_product, name="delete"),
    path('reduce/<int:product_id>/', views.reduce_product, name="reduce"),
    path('clean/', views.clear_cart, name="clear"),
]
