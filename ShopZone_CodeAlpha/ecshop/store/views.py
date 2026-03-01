from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Product, Category, Order, OrderItem
import json

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    featured = Product.objects.filter(is_featured=True)[:4]
    
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search', '')
    
    if category_slug:
        products = products.filter(category__slug=category_slug)
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'featured': featured,
        'search_query': search_query,
        'active_category': category_slug,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related': related,
    })

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('home')
    return render(request, 'store/auth.html', {'mode': 'register'})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'store/auth.html', {'mode': 'login'})

def logout_view(request):
    logout(request)
    return redirect('home')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(pk=int(pid))
            subtotal = product.price * qty
            total += subtotal
            cart_items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    key = str(pk)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    request.session.modified = True
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'count': sum(cart.values())})
    messages.success(request, f'{product.name} added to cart!')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    key = str(pk)
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

def update_cart(request, pk):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        key = str(pk)
        qty = int(request.POST.get('quantity', 1))
        if qty > 0:
            cart[key] = qty
        else:
            cart.pop(key, None)
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart')

@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')
    
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(pk=int(pid))
            subtotal = product.price * qty
            total += subtotal
            cart_items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass
    
    if request.method == 'POST':
        address = request.POST.get('address', '')
        order = Order.objects.create(user=request.user, total_price=total, address=address)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['product'].price)
        request.session['cart'] = {}
        request.session.modified = True
        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('order_success', pk=order.id)
    
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'store/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/my_orders.html', {'orders': orders})
