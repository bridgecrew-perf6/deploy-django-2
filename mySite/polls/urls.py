from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.shop, name='shop'),
    path('loginv4', views.loginv4, name='shop'),
    path('login/', views.login, name='login'),
    path('home/', views.eventLogin, name='elogin'),
    path('shop/', views.sign_up, name='sign_up'),
    path('cart/',views.cart,name='cart'),
    path('detail/<int:id_product>',views.product_detail,name='detail'),
    path('setcookie',views.setcookie),
    path('getcookie',views.getcookie),
    
# API

    path('products/<int:product_id>/', views.getProductById),
    path('products',views.getAllProduct),
    path('home/products',views.getAllProduct),
    path('home/products/<int:product_id>/', views.getProductById),
    path('cart/cartitem/',views.getCartItem),
    path('cart/delete/<int:id>',views.delete_item), 
    path('add_to_cart/<int:id>',views.add_to_cart), 

]   
     