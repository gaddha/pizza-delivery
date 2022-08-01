from django.urls import path
from .views import helloordersview
from . import views


urlpatterns = [
  path('orders/',helloordersview.as_view(),name='helloorders'),
  path('',views.orderCreateView.as_view(),name='listorders'),
  path('<int:order_id>/',views.orderDetailView.as_view(),name = 'order_detail'),
  path('staus-update/<int:order_id>/',views.UpdateOrderStatus.as_view(),name = 'order_status_Update'),
  path('user/<int:user_id>/order/',views.UserOrdersView.as_view(),name = 'users_orders_view'),
  path('user/<int:user_id>/order/<int:order_id>/',views.userOrderDetialsView.as_view(),name = 'users_spec_orders'),
  ]