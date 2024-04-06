from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def order_page(request):
    return render(request, 'order.html')

#register
def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '등록 성공!')  # 등록 성공 메시지 추가
            return redirect('register')  # 같은 페이지로 리다이렉트하여 메시지 표시
    else:
        form = CustomerForm()
    
    return render(request, 'register.html', {'form': form})