from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        cost_price = request.POST['cost_price']
        selling_price = request.POST['selling_price']
        kol_day = request.POST['kol_day']
        supplier_url = request.POST.get('supplier_url') 
        product = Product(name=name, cost_price=cost_price, selling_price=selling_price, kol_d=kol_day, supplier_url=supplier_url)
        product.save()
        return redirect('index')
    return render(request, 'business_total_gen_app/add_product.html')


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('index')

def index(request):
    products = Product.objects.all()

    kol_day = sum(product.kol_d for product in products)
    costs = sum(product.cost_price for product in products) * kol_day
    revenue = sum(product.selling_price for product in products) * kol_day

    profit = revenue - costs

    kol_day_m = sum(product.kol_d for product in products) * 30
    costs_m = sum(product.cost_price for product in products) * kol_day * 30
    revenue_m = sum(product.selling_price for product in products) * kol_day * 30

    profit_m = (revenue - costs) * 30

    context = {
        'products': products,
        'revenue': revenue,
        'costs': costs,
        'profit': profit,
        'kol_day': kol_day,
        'revenue_m': revenue_m,
        'costs_m': costs_m,
        'profit_m': profit_m,
        'kol_day_m': kol_day_m,
    }

    return render(request, 'business_total_gen_app/index.html', context)
