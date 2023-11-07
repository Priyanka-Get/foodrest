from django import forms
from .models import Restaurant, Category,FoodItem,FoodItemStatus,Customer,Order,Employee

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'restaurant']




class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'description', 'price', 'restaurant', 'category']

    def _init_(self, *args, **kwargs):
        super(FoodItemForm, self)._init_(*args, **kwargs)

class FoodItemStatusForm(forms.ModelForm):
    class Meta:
        model = FoodItemStatus
        
        fields = ['name', 'restaurant', 'category', 'food_item']
        labels ={
            'name':'status'
            }

    def _init_(self, *args, **kwargs):

        super(FoodItemStatusForm, self)._init_(*args, **kwargs)   




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def _init_(self, *args, **kwargs):
        super(CustomerForm, self)._init_(*args, **kwargs)       

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def _init_(self, *args, **kwargs):
        super(OrderForm, self)._init_(*args, **kwargs)  

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
