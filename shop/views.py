from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def home(request, c_slug=None):
    c_page = None
    prodt = None
    global cat, pro
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        prodt = Prod.objects.filter(category=c_page, available=True)
    else:
        prodt = Prod.objects.all().filter(available=True)
        cat = Category.objects.all()
        paginator = Paginator(prodt, 6)
        try:
            page = int(request.GET.get('page', '1'))
        except():
            page = 1
        try:
            pro = paginator.page(page)
        except(EmptyPage, InvalidPage):
            pro = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro})


def product_details(request, c_slug, product_slug):
    try:
        prod = Prod.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'product.html', {'pr': prod})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Prod.objects.all().filter(Q(name__contains=query) | Q(des__contains=query))

    return render(request, 'search.html', {'qr': query, 'pr': prod})


def filtering(request, c_slug):
    c_page = None
    prodt = None
    global cat, pro
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        prodt = Prod.objects.filter(category=c_page, available=True)
    else:
        prodt = Prod.objects.all().filter(available=True)
        cat = Category.objects.all()

    return render(request, 'filter.html', {'pr': prodt, 'ct': cat})
