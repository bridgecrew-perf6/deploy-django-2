from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.shop, name='shop'),
    path('login/', views.login, name='login'),
    path('home/', views.eventLogin, name='elogin'),
    path('shop/', views.sign_up, name='sign_up'),
    path('shop/<int:product_id>/', views.viewProductById, name='byid'),
    path('cart/',views.cart,name='cart'),
    path('detail/<int:id_product>',views.product_detail,name='detail')
]
    