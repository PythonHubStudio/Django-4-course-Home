from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/', views.CartAddView.as_view(), name='cart_add'),
    path('cart_change/', views.CartChangeView.as_view(), name='cart_change'),
    path('cart_remove/', views.CartRemoveView.as_view(), name='cart_remove'),
]