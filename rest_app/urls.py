


from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.base, name='base'),
   

    path('category_list/', views.category_list, name='category_list'),
    path('category_create/', views.category_create, name='category_create'),
    path('category_update/<int:pk>/', views.category_update, name='category_update'),
    path('category_delete/<int:pk>/', views.category_delete, name='category_delete'),


    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('restaurant_create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant_update/<int:pk>/', views.restaurant_update, name='restaurant_update'),
    path('restaurant_delete/<int:pk>/', views.restaurant_delete, name='restaurant_delete'),


      
    path('fooditem_list/', views.fooditem_list, name='fooditem_list'),
    path('fooditem_create/', views.fooditem_create, name='fooditem_create'),
    path('fooditem_update/<int:pk>/', views.fooditem_update, name='fooditem_update'),
    path('fooditem_delete/<int:pk>/', views.fooditem_delete, name='fooditem_delete'),


    path('fooditemstatus_list/', views.fooditemstatus_list, name='fooditemstatus_list'),
    path('fooditemstatus_create/', views.fooditemstatus_create, name='fooditemstatus_create'),
    path('fooditemstatus_update/<int:pk>/', views.fooditemstatus_update, name='fooditemstatus_update'),
    path('fooditemstatus_delete/<int:pk>/', views.fooditemstatus_delete, name='fooditemstatus_delete'),



    
    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer_create/', views.customer_create, name='customer_create'),
    path('customer_update/<int:pk>/', views.customer_update, name='customer_update'),
    path('customer_delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    

   

    path('order_list/', views.order_list, name='order_list'),
    path('order_create/', views.order_create, name='order_create'),
    path('order_update/<int:pk>/', views.order_update, name='order_update'),
    path('order_delete/<int:pk>/', views.order_delete, name='order_delete'),


    path('employee-list/', views.employee_list, name='employee_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('edit-employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:pk>/', views.delete_employee, name='delete_employee'),

   



    


    
]