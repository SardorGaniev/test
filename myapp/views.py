from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *

from cart.cart import Cart

def func(request):
    return render(request, 'myapp/index.html',)

def menu(request):
    items = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=items)
    items = myFilter.qs

    context = {
        'items': items,
        'myFilter': myFilter
        # 'cart': cart
    }
    return render(request, 'myapp/menu.html', context)

def about(request):
    return render(request, 'myapp/about.html')

@login_required(login_url='login')
def add_stuff(request):
    form = StuffForm
    if request.method == 'POST':
        form = StuffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Вы успешно добавили повара.')
            return redirect('add_stuff')
        else:
            messages.info(request, 'ОШИБКА')
    items = Stuff.objects.all()
    context = {
        "form": form,
        "items": items,
    }
    return render(request, 'myapp/add_stuff.html', context)

@login_required(login_url='login')
def add_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Вы успешно добавили продукт.')
            return redirect('add_product')
        else:
            messages.info(request, 'ОШИБКА')
    items = Product.objects.all()
    context = {
        "form": form,
        "items": items,
    }
    return render(request, 'myapp/add_product.html', context)

def stuff(request):
    stuffs = Stuff.objects.all()
    context = {
        'stuffs': stuffs,
    }
    return render(request, 'myapp/stuff.html', context)

def gallery(request):
    return render(request, 'myapp/gallery.html')

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Вы успешно оставили отзыв о нашем продукте. Благодарим за отзыв')
            return redirect('contact')
        else:
            messages.info(request, 'ОШИБКА')
    items = Product.objects.all()

    context = {
        'items': items
    }
    return render(request, 'myapp/contact.html', context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')
            else:
                messages.success(request, "ОШИБКА")
                return redirect('register')
        context = {'form': form}
        return render(request, 'login_app/reg.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                messages.info(request, "ОШИБКА")

        context = {}

        return render(request, 'login_app/reg.html', context)

def logout_page(request):
    logout(request)
    return redirect('register')

@login_required(login_url='login')
def cart_page(request):
    return render(request, 'myapp/cart.html')

@login_required(login_url='login')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("menu")

@login_required(login_url='login')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")

@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")

@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")

@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")

@login_required(login_url="login")
def delete_p(request, pk):
    data = Product.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('homepage')
    context = {
        "data": data,
    }
    return render(request, 'myapp/delete_product.html', context)

@login_required(login_url="login")
def update_p(request, pk):
    Product1 = Product.objects.get(id=pk)
    data = ProductupdateForm(instance=Product1)
    if request.method == "POST":
        form = ProductupdateForm(request.POST, instance=Product1)
        if form.is_valid:
            form.save()
            return redirect('homepage')

        else:
            messages.info(request, 'ОШИБКА')
    context = {
        "data": data
    }
    return render(request, "myapp/update_product.html", context)


def product_detail(request, id):
    data = Product.objects.get(pk=id)
    return render(request, 'myapp/detail.html', {'data': data})



