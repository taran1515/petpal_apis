from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from product import views
from product.views import PostDetail,PostDetailCreate,ProductDetail,AddressDetail,CancelOrderDetail
urlpatterns = [
    path('api/v1/get_products/',views.get_products),
    path('api/v1/get_product/<int:id>/',ProductDetail.as_view()),
    path('api/v1/post_product/',views.post_product),
    path('api/v1/get_addresses/',views.get_addresses),
    path('api/v1/post_address/',views.post_address),
    path('api/v1/get_address/<int:id>/',AddressDetail.as_view()),
    path('api/v1/get_medicines/',views.medicine_list),
    path('api/v1/medicine_search/',views.medicine_search),
    path('api/v1/get_cancel_orders/',views.get_cancel_orders),
    path('api/v1/post_cancel_order/',views.post_cancel_order),
    path('api/v1/get_cancel_order/<int:id>',CancelOrderDetail.as_view()),
    path('api/v1/post/<int:id>/',PostDetail.as_view()),
    path('api/v1/post/',PostDetailCreate.as_view())


]