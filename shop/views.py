from django.shortcuts import render, get_object_or_404
from .models import Category, Product ,Subcategory
from cart.forms import CartAddProductForm

def subcategories_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = subcategories.filter(category=category)
    return render(request,
                  'shop/product/subcategories.html',
                  {'category': category,
                   'categories': categories,
                   'subcategories': subcategories})

def product_list(request, subcategory_slug=None):
    subcategory = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.all()
    if subcategory_slug:
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        products = products.filter(subcategory=subcategory)
    return render(request,
                  'shop/product/list.html',
                  {'subcategory': subcategory,
                   'subcategories': subcategories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                )
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form' : cart_product_form})

# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request,
                  'shop/product/index.html',
                  {'categories': categories,
                   'products': products})