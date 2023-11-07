









from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant,Category,FoodItem,FoodItemStatus,Customer,Order,Employee


from django.shortcuts import render, redirect
from .forms import RestaurantForm,CategoryForm,FoodItemForm,FoodItemStatusForm,CustomerForm,OrderForm,EmployeeForm

# dashboard-----------

def base(request):
    return render(request,"rest_app/base.html")




# -------restaurant------
def restaurant_list(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'rest_app/restaurant_list.html', {'restaurant': restaurant})

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'rest_app/restaurant_create.html', {'form': form})
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'rest_app/restaurant_update.html', {'form': form})

def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list') 
    return render(request, 'rest_app/restaurant_delete.html', {'restaurant': restaurant})  

  

#   category------------

def category_list(request):
    category = Category.objects.all()
    return render(request, 'rest_app/category_list.html', {'category':  category })


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'rest_app/category_create.html', {'form': form})
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'rest_app/category_update.html', {'form': form})   



def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list') 
    return render(request, 'rest_app/category_delete.html', {'category': category})  



# fooditem-----

def fooditem_list(request):
    fooditem = FoodItem.objects.all()
    return render(request, 'rest_app/fooditem_list.html', {'fooditem': fooditem})

  

def fooditem_create(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fooditem_list')
    else:
        form = FoodItemForm()
    return render(request, 'rest_app/fooditem_create.html', {'form': form})
def fooditem_update(request, pk):
    fooditem = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=fooditem)
        if form.is_valid():
            form.save()
            return redirect('fooditem_list')
    else:
        form = FoodItemForm(instance=fooditem)
    return render(request, 'rest_app/fooditem_update.html', {'form': form})  



def fooditem_delete(request, pk):
    fooditem = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        fooditem.delete()
        return redirect('fooditem_list') 
    return render(request, 'rest_app/fooditem_delete.html', {'fooditem': fooditem}) 



def fooditemstatus_list(request):
    fooditemstatus = FoodItemStatus.objects.all()
    return render(request, 'rest_app/fooditemstatus_list.html', {'fooditemstatus': fooditemstatus})    


def fooditemstatus_create(request):
    if request.method == 'POST':
        form = FoodItemStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fooditemstatus_list')
    else:
        form = FoodItemStatusForm()
    return render(request, 'rest_app/fooditemstatus_create.html', {'form': form})
def fooditemstatus_update(request, pk):
    fooditemstatus = get_object_or_404(FoodItemStatus, pk=pk)
    if request.method == 'POST':
        form = FoodItemStatusForm(request.POST, instance=fooditemstatus)
        if form.is_valid():
            form.save()
            return redirect('fooditemstatus_list')
    else:
        form = FoodItemStatusForm(instance=fooditemstatus)
    return render(request, 'rest_app/fooditemstatus_update.html', {'form': form})  



def fooditemstatus_delete(request, pk):
    fooditemstatus = get_object_or_404(FoodItemStatus, pk=pk)
    if request.method == 'POST':
        fooditemstatus.delete()
        return redirect('fooditemstatus_list') 
    return render(request, 'rest_app/fooditemstatus_delete.html', {'fooditemstatus': fooditemstatus})




    # -----customers-----

def customer_list(request):
    customer = Customer.objects.all()
    return render(request, 'rest_app/customer_list.html', {'customer':  customer })


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'rest_app/customer_create.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'rest_app/customer_update.html', {'form': form})   



def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list') 
    return render(request, 'rest_app/customer_delete.html', {'customer': customer})




    # -----order-----

def order_list(request):
    order = Order.objects.all()
    return render(request, 'rest_app/order_list.html', {'order':  order })


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'rest_app/order_create.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'rest_app/order_update.html', {'form': form})   



def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list') 
    return render(request, 'rest_app/order_delete.html', {'order': order})


# User----------------

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'rest_app/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'rest_app/add_employee.html', {'form': form})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'rest_app/edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'rest_app/delete_employee.html', {'employee': employee})    



 
