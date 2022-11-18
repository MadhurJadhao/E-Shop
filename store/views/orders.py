from django.shortcuts import render, redirect
from django.views import View 
from store.models.customer import Customer
from store.models.product import Product
from store.models.oders import Order
from store.middleware.auth import auth_middleware 
 
 
class OderView(View):
    
    def get(self, request):
        customer = request.session.get('customer')
        oders = Order.get_order_by_customer(customer)
        print(oders)
        oders = oders.reverse()
        return render(request, 'orders.html', {'orders' : oders})
      