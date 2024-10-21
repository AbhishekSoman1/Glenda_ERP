

from django.urls import path,include

from Glenda_App import views
from Glenda_App.views import raw_materials_data

urlpatterns = [
    path('',views.index,name='index'),
    path('create_menu', views.create_menu, name='create_menu'),
    path('create_submenu', views.create_submenu, name='create_submenu'),
    path('calendar', views.calendar, name='calendar'),
    # path('pie-chart/', views.pie_chart_view, name='pie_chart'),
    path('api/raw-materials/', raw_materials_data, name='raw_materials_data'),  # API endpoint
    # path('stock-data/', stock_data, name='stock_data'),

]
