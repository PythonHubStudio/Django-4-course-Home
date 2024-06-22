from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(), name='create_order'),
]