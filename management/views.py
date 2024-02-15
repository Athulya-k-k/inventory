from django.shortcuts import render, redirect
from .models import Product,Sale
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import SaleForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/update_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

def send_restock_notification(product):
    subject = f'Restock Notification: {product.name}'
    message = f'The quantity of {product.name} is low and needs restocking.'
    from_email = 'your@email.com'
    to_email = 'recipient@email.com'
    send_mail(subject, message, from_email, [to_email])



def record_sale(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            quantity_sold = form.cleaned_data['quantity_sold']
            if product.record_sale(quantity_sold):
                Sale.objects.create(product=product, quantity_sold=quantity_sold)
                return redirect('product_list')
            else:
                # Handle case where not enough quantity is available
                pass
    else:
        form = SaleForm()
    return render(request, 'inventory/record_sale.html', {'product': product, 'form': form})


def best_selling_products(request):
    # Query to find best-selling products based on total quantity sold
    best_selling_products = Product.objects.annotate(total_quantity_sold=models.Sum('sale__quantity_sold')).order_by('-total_quantity_sold')[:10]
    return render(request, 'inventory/best_selling_products.html', {'best_selling_products': best_selling_products})