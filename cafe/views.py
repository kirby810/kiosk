from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer

# Create your views here.

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

#register
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