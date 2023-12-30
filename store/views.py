from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category, SELLER, warranty_period, PRODUCT_BY
from django.core.paginator import Paginator
from django.db.models import Q

def category(request, category_slug=None):

    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 6)  
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    categories = Category.objects.all()
    sellers = SELLER.objects.all()
    warranties = warranty_period.objects.all()
    types = PRODUCT_BY.objects.all()

    context = {'products': paged_product, 'categories': categories, 'type': types, 'warranty': warranties, 'Seller': sellers}
    print(context)
    return render(request, 'store/store.html',  context)

def products_by_seller(request,  seller_id):
    seller = get_object_or_404(SELLER,   id=seller_id)

    products = Product.objects.filter(is_available=True,   Seller=seller)

    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    categories = Category.objects.all()
    sellers = SELLER.objects.all()
    warranties = warranty_period.objects.all()
    types = PRODUCT_BY.objects.all()

    context = {'products': paged_product,   'categories': categories, 'type': types, 'warranty': warranties, 'Seller': sellers}

    return render(request, 'store/store.html',   context)



def products_by_warranty(request, warranty_period_id):
    warranty_obj = get_object_or_404(warranty_period, id=warranty_period_id)
    products = Product.objects.filter(is_available=True, Warranty=warranty_obj)

    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    categories = Category.objects.all()
    sellers = SELLER.objects.all()
    warranties = warranty_period.objects.all()
    types = PRODUCT_BY.objects.all()

    context = {'products': paged_product,  'categories': categories,   'type': types, 'warranty': warranties, 'Seller': sellers}

    return render(request, 'store/store.html',  context)


def products_by_type(request,  product_by_id):
    product_type = get_object_or_404(PRODUCT_BY, id=product_by_id)
    products = Product.objects.filter(is_available=True,  Product=product_type)

    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    categories = Category.objects.all()
    sellers = SELLER.objects.all()
    warranties = warranty_period.objects.all()
    types = PRODUCT_BY.objects.all()

    context = {'products': paged_product, 'categories': categories, 'type': types, 'warranty': warranties, 'Seller': sellers}

    return render(request, 'store/store.html', context)




def store2(request, category_slug=None):
    sort = request.GET.get('sort', 'asc') 
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        category = get_object_or_404(SELLER, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category)
    else:
        products = Product.objects.filter(is_available=True)
    
    if sort == 'asc':
        products = products.order_by('price')
    elif sort == 'desc':
        products = products.order_by('-price')

    page = request.GET.get('page')
    paginator = Paginator(products, 12)
    paged_products = paginator.get_page(page)

    categories = Category.objects.all()
    sellers = SELLER.objects.all()
    warranties = warranty_period.objects.all()
    types = PRODUCT_BY.objects.all()

    context = {'products': paged_products, 'categories': categories, 'type': types, 'warranty': warranties, 'Seller': sellers}

    return render(request, 'store/store.html', context)


def search(request):
    products = Product.objects.filter(is_available=True)

    q = request.GET.get('q')
    if q:
        products = products.filter(
            Q(category__category_name__icontains=q)|  
            Q(Product__category_name__icontains=q) | 
            Q(Warranty__category_name__icontains=q)| 
            Q(Seller__category_name__icontains=q)| 

            Q(product_name__icontains=q)| 
            Q(price__icontains=q)    
        )

 
    paginator = Paginator(products, 5) 
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    categories = Category.objects.all()
    sellers = SELLER.objects.all()
    warranties = warranty_period.objects.all()
    types = PRODUCT_BY.objects.all()

    context = {'products': paged_product, 'categories': categories, 'type': types, 'warranty': warranties, 'Seller': sellers}

    return render(request, 'store/store.html', context)
