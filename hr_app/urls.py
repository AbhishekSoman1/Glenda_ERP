from django.urls import path
from hr_app import views
urlpatterns = [
    path('Employee_list',views.Employee_list,name='Employee_list'),
    path('AddDetails',views.AddDetails,name='AddDetails')
]