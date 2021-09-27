from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),

    # Add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    # Contact Path
    path('contact/', views.contact_us, name='contact'),

    #Checkout Page
    path('checkout/', views.Checkout, name='checkout'),

    #Order Page
    path('order/', views.Your_Order, name='order'),

    #Product Page
    path('product/', views.Your_Product, name='product'),

     #Product Page
    path('product/<str:id>/', views.Product_Detail, name='product_detail'),

    #Product Page
    path('search/', views.Search, name='search'),
]