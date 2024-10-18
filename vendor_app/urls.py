from django.urls import path

from vendor_app import views

urlpatterns = [
    path('vender_register_view', views.vender_register_view, name='vender_register_view'),
    path('view_vendor_list', views.view_vendor_list, name='view_vendor_list'),
    path('create_vendor_details/<int:id>', views.create_vendor_details, name='create_vendor_details'),

]