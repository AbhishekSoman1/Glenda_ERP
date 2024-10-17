

from django.urls import path,include

from Glenda_App import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create_menu', views.create_menu, name='create_menu'),
    path('create_submenu', views.create_submenu, name='create_submenu'),
    path('calendar', views.calendar, name='calendar'),

]
