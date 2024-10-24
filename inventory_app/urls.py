

from django.urls import path

from inventory_app import views

urlpatterns = [
    path('Raw_materials_view', views.raw_materials_view, name='Raw_materials_view'),
    path('update_stocks/<int:id>', views.update_stocks, name='update_stocks'),
    path('finishedgoods_stock_view', views.finishedgoods_stock_view, name='finishedgoods_stock_view'),
    path('update_finished_goods_stocks/<int:id>', views.update_finished_goods_stocks, name='update_finished_goods_stocks'),

]