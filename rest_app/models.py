from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  


class FoodItemStatus(models.Model):
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    

    def __str__(self):
        return self.name   

class OrderStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    

class Customer(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    food_item = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')

    def __str__(self):
        return self.name   

    def __str__(self):
        return self.quantity 

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.ManyToManyField(Customer)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')

    def __str__(self):
        return f"Order for {self.food_item.name} in {self.restaurant.name}"
    
    
        




class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=20)

    def str(self):
        return self.name        

