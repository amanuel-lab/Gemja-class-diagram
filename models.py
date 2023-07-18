from email.policy import default
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default='avatar.jpeg' ,upload_to='Pictures')

    def __str__(self) -> str:
        return self.user.username

class Supplier(models.Model):
    ids = models.CharField(max_length=100, null=True)
    suppliername = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return self.suppliername
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=100, null=True)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.product} ordered quantity {self.order_quantity}'
    
class Store(models.Model):
    identification = models.CharField(max_length=100, null=True)
    storename = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.storename

class dispatched(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    created_by = models.ForeignKey(User, models.CASCADE, default=None)
    order_quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    storename = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.product} ordered quantity {self.order_quantity}'

