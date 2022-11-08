from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request, cart_cnt=0, user_active=None):
    return render(request, 'main_site/index.html',
                  {
                      'user': user_active,
                      'cart_count': cart_cnt
                  })


def product_list(request, category_slug):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/catalog/list.html',
                  {
                      'categoty': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/catalog/detail.html')


def about(request, cart_cnt=0, user_active=None):
    return render(request, 'main_site/about.html',
                  {
                      'user': user_active,
                      'cart_count': cart_cnt
                  })


def installment(request, cart_cnt=0, user_active=None):
    return render(request, 'info/installments.html',
                  {
                      'user': user_active,
                      'cart_count': cart_cnt
                  }
                  )


def payments(request, cart_cnt=0, user_active=None):
    return render(request, 'info/payments.html',
                  {
                      'user': user_active,
                      'cart_count': cart_cnt
                  }
                  )


def rules(request):
    return render(request, 'info/rules.html')


def offer(request, cart_cnt=0, user_active=None):
    return render(request, 'info/offer.html',
                  {
                      'user': user_active,
                      'cart_count': cart_cnt
                  }
                  )


def policy(request, cart_cnt=0, user_active=None):
    return render(request, 'info/policy.html',
                  {
                      'user': user_active,
                      'cart_count': cart_cnt
                  }
                  )


def exchange(request):
    return render(request, 'info/exchange.html')


def delivery(request):
    return render(request, 'info/delivery.html')
