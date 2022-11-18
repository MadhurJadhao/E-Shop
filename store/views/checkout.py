from django.shortcuts import render, redirect
from django.views import View 
from store.models.customer import Customer
from store.models.product import Product
from store.models.oders import Order
 
class CheckOut(View):
    def post(self, request):
       address = request.POST.get('address')
       phone = request.POST.get('phone')
       customer = request.session.get('customer')
       cart = request.session.get('cart')
       products = Product.get_products_by_id(list(cart.keys()))
       print(address, phone, customer, cart, products)
       
       for product in products:
           print(cart.get(str(product.id)))
           orders = Order(Customer = Customer(id=customer),
                        product = product, 
                        price = product.price,
                        address = address,
                        phone = phone, 
                        quantity = cart.get(str(product.id)))
           
           orders.save()
           
       request.session['cart'] = {}
       return redirect('cart')
    