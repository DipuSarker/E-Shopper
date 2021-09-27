from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from cart.cart import Cart
from .models import *
from .forms import *

# Create your views here.

def master(request):
    return render(request,'master.html')


def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    brand = Brand.objects.all()

    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')

    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product,
        'brand': brand
    }
    return render(request,'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact.save()
    return render(request, 'contact.html')


def Checkout(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            order = Order(
                product = cart[i]['name'],
                image = cart[i]['image'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                user = user,
                phone = phone,
                pincode = pincode,
                address = address,
                total = total
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')

    return HttpResponse('This is checkout page')


def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user)

    context = {'order': order}

    return render(request, 'order.html', context)


def Your_Product(request):
    category = Category.objects.all()
    product = Product.objects.all()
    brand = Brand.objects.all()

    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')

    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product,
        'brand': brand
    }
    return render(request, 'product.html', context)


def Product_Detail(request, id):
    product = Product.objects.filter(id=id).first()
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains=query)
    context = {'product': product}
    return render(request, 'search.html', context)


@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')