from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default='null')
    address = models.CharField(max_length=300, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    
    
    def placeOrder(self):
        self.save()
        
        
    @staticmethod
    def get_order_by_customer(customer_id):
        return Order\
            .objects\
            .filter(Customer = customer_id)\
            .order_by('date')    