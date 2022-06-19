from django.urls import path
from . import views
urlpatterns = [
    path('cart_details/', views.cart, name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='add_cart'),
    path('dec/<int:product_id>/', views.min_cart, name='decrement'),
    path('del/<int:product_id>/', views.del_cart, name='delete'),
]
