from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer,Menu, Order



def home(request):
    return render(request, 'home.html')

def order_page(request):
    message = None

    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')
        
        try:
            customer = Customer.objects.get(phone_num=phone_num)
            return render(request, 'order_detail.html', {'customer': customer})
        except Customer.DoesNotExist:
            message = '고객 정보가 없습니다.'

    return render(request, 'order.html', {'message': message})


def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '등록 성공!')  
            return redirect('register') 
    else:
        form = CustomerForm()
    
    return render(request, 'register.html', {'form': form})


def order_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    menus = Menu.objects.all()
    
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        
        for menu in menus:
            quantity = request.POST.get(f'quantity_{menu.id}')
            
            if quantity:
                order = Order(customer_id_id=customer_id, menu_id_id=menu.id, quantity=quantity)
                order.save()
        
        messages.success(request, '주문 성공!')
        return redirect('home')
    
    # GET 요청 처리
    return render(request, 'order_detail.html', {'customer': customer, 'menus': menus})
