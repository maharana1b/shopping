from django.shortcuts import render
from django.views import View
from .models import *



class ProductView(View):
    def get(self,request):
        topwares = Product.objects.filter(category='TW')
        bottomware = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')

        return render(request,'app/home.html',{'topwares':topwares,'bottomware':bottomware,'mobile':mobile,'laptop':laptop})


class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)

        return render(request,'app/productdetail.html',{'product':product})


def BottomWare(request, data=None):
    if data == None:
        bottomware = Product.objects.filter(category='BW')
    elif data == 'Lee' or data == 'Wrangler':
        bottomware = Product.objects.filter(category='BW').filter(brand=data)
    return render(request, 'app/mobile.html')





def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
