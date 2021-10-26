from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProductForm, OrderForm, CreateUserForm
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

    context = {'form':form}
    return render(request, 'orders/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'orders/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()

    total_products = products.count()
    total_orders = orders.count()

    order_number = request.GET.get('order_number')
    item_name = request.GET.get('item_name')

    if item_name != '' and item_name is not None and item_name:
        products = products.filter(title=item_name)

    if order_number != '' and order_number is not None:
        orders = orders.filter(order_number=order_number)
    


    context = {
        'orders': orders,
        'products':products,
        'total_products': total_products,
        'total_orders': total_orders,
    }
    return render(request, 'orders/home.html', context)


@login_required(login_url='login')
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form
    }
    return render(request, 'orders/order_form.html',context)


@login_required(login_url='login')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'orders/order_form.html',context)


@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/')
    context = {
        'item':product
    }
    return render(request, 'orders/delete.html', context)


@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form
    }
    return render(request, 'orders/order_form_c.html',context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {
        'item':order
    }
    return render(request, 'orders/delete_o.html', context)
