from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View



class Singup(View):
    def get(self, request):
        return render(request, 'singup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password') 
       #vaition
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
                
        }
        error_msg = None
        
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password,)
        error_msg = self.validateCustomer(customer)
             
        #saving
        if not error_msg:
            print(first_name,last_name,phone,email,password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:    
            data = {
                'error' : error_msg,
                 'values' : value
            }
            return render(request, 'singup.html', data)
  
    def validateCustomer(self,customer):
        error_msg = None
        if(not customer.first_name):
            error_msg = 'First Name Required..!!'
        elif len(customer.first_name) < 4:
            error_msg = 'First name must be 4 char long or more..'
        elif (not customer.last_name):
            error_msg = 'Last Name Require..!!'
        elif len(customer.last_name) < 4:
            error_msg = 'Last name must be 4 char long or more..'
        elif (not customer.phone):
            error_msg = 'Phone Number Required'
        elif len(customer.phone) < 10:
            error_msg = 'Phone Number Must be 10 Number'
        elif len(customer.password) < 8:
            error_msg = 'Password Must Be 8 Charector Long'
        elif len(customer.email) < 8:
            error_msg = 'Email Must be 8 chrector Long'    
        
        elif customer.isExists():
            error_msg = 'Email Address Already Register..'  
        return error_msg

  
    
    
        
  