from django.urls import path
from .import views

urlpatterns = [
    path('', views.func, name='homepage'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('stuff/', views.stuff, name='stuff'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),

    path('add_stuff/', views.add_stuff, name='add_stuff'),
    path('add_product/', views.add_product, name='add_product'),

    path('product/<int:id>/', views.product_detail, name='product'),
    path('update_p/<str:pk>', views.update_p, name="update_p"),
    path('delete_p/<int:pk>', views.delete_p, name="delete_p"),

    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),

    path('cart/', views.cart_page, name='cart'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
]