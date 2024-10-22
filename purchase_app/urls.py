


from django.urls import path

from purchase_app import views

urlpatterns = [
    path('manager_home', views.manager_home, name='manager_home'),
    path('add_category',views.add_category,name='add_category'),
    path('create_raw_material',views.create_raw_material,name='create_raw_material'),
    path('view_rawmaterials',views.view_rawmaterials,name='view_rawmaterials'),
    path('update_rawmaterials/<int:id>', views.update_rawmaterials, name='update_rawmaterials'),
    path('delete_raw/<int:id>', views.delete_rawmaterils, name='delete_raw'),

]